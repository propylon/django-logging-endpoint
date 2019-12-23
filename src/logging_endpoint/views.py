# -*- coding: utf-8 -*-
"""views module for logging_endpoint package.

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
from __future__ import unicode_literals

import json
import logging

from django.http import HttpResponse
from django.utils.module_loading import import_string
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import six
from logging_endpoint.settings import LOGGER, MESSAGE_HANDLER

logger = logging.getLogger(LOGGER)
if isinstance(MESSAGE_HANDLER, six.string_types):
    MESSAGE_HANDLER = import_string(MESSAGE_HANDLER)

try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError


@csrf_exempt
@require_POST
def get_messages(request):
    """Return the messages in the given request.

    If the body is json deserializable, a list is decomposed to individual
    messages.
    """
    try:
        content = json.loads(request.body)
        if isinstance(content, list):
            return content

        return [content]
    except JSONDecodeError:
        return [request.body]


def logging_view(request):
    """Send the received logs to the logger."""
    for message in get_messages(request):
        msg_logger, level, msg, args, kwargs = MESSAGE_HANDLER(message)
        if not msg_logger:
            msg_logger = logger

        msg_logger.log(level, msg)

    return HttpResponse(status=200)
