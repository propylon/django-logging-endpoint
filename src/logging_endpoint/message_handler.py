# -*- coding: utf-8 -*-
"""message handler module for logging_endpoint package.

Copyright 2019 Propylon Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from logging import INFO, getLevelName

from logging_endpoint.settings import OVERWRITE_LOGGER


def default_handler(log_data):
    """Return the message as is as level INFO on the default logger."""
    if isinstance(log_data, bytes):
        log_data = log_data.decode()
    return None, INFO, str(log_data), tuple(), dict()


def json_handler(log_data):
    """Return the message based on a json dictionary.

    Example input:
    {
        'message':   'my log message',
        'logger':    'user interaction',
        'loglevel':  'error',
        'timestamp': '2020-01-01T12:00Z'
    }

    Results in:
    * Log message of the given loglevel
    * If the setting OVERWRITE_LOGGER is set, the given logger is used.
      Otherwise the standard logger is used, but the given one is added to the
      complete message
    * The timestamp is added to the log message

    -> ERROR - 2020-01-01T12:00Z - user interaction - my log message
    """
    logger = log_data.get('logger', None)
    level = getLevelName(log_data.get('loglevel', 'INFO').upper())
    msg = '-'.join(filter(None, (
        log_data.get('timestamp', ''),
        logger,
        str(log_data.get('message', None))
    )))
    args = tuple()
    kwargs = dict()

    return (
        logger if logger and OVERWRITE_LOGGER else None,
        level,
        msg,
        args,
        kwargs
    )
