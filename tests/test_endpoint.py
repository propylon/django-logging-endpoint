# -*- coding: utf-8 -*-
"""Endpoint tests."""
import json
import logging

import pytest


@pytest.fixture(autouse=True)
def loglevel(caplog):
    caplog.set_level(logging.DEBUG, logger='LoggingEndpoint')


@pytest.mark.parametrize('input, expected', [
    ('test', 'test'),
    ('test2, test3', 'test2, test3')
])
def test_default_handler(client, caplog, input, expected):
    response = client.post('/logs/', input, content_type='text/plain')
    assert response.status_code == 200
    assert caplog.records[0].message == expected


@pytest.mark.parametrize('input, expected', [
    ({'message': 'test'}, [('test', logging.INFO)]),
    ([
        {'message': 'test'},
        {'message': 'test2'}
    ], [
        ('test', logging.INFO),
        ('test2', logging.INFO),
    ]),
    ([{
        'timestamp': '2020-01-01T12:00:00Z',
        'message': 'testmessage',
        'loglevel': 'debug'
    }], [('2020-01-01T12:00:00Z testmessage', logging.DEBUG)])
])
def test_json_handler(client, caplog, input, expected):
    response = client.post(
        '/logs/',
        data=json.dumps(input),
        content_type='application/json'
    )
    assert response.status_code == 200
    for log in caplog.records:
        assert log.message, log.level == expected
