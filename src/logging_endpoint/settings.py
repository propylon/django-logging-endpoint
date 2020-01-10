# -*- coding: utf-8 -*-
"""Settings module for logging_endpoint package.

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
from django.conf import settings

DECOMPOSE_JSON_LISTS = getattr(
    settings,
    'LOGGING_ENDPOINT_DECOMPOSE_JSON_LISTS',
    True
)

LOGGER = getattr(settings, 'LOGGING_ENDPOINT_LOGGER', 'LoggingEndpoint')

MESSAGE_HANDLER = getattr(
    settings,
    'LOGGING_ENDPOINT_MESSAGE_HANDLER',
    'logging_endpoint.message_handler.default_handler'
)

OVERWRITE_LOGGER = getattr(
    settings,
    'LOGGING_ENDPOINT_OVERWRITE_LOGGER',
    False
)
