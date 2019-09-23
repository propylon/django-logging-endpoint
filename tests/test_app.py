import logging_endpoint
from logging_endpoint.apps import LoggingEndpointConfig


def test_app_initialization():
    assert LoggingEndpointConfig('logging_endpoint', logging_endpoint)
