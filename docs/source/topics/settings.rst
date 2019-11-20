.. _settings:

Settings
--------
logging_endpoint is configured by adding the following settings to the Django
settings.

.. py:attribute:: LOGGER

      The name of the logger to send the received logs to.

      Default
         :code:`'LoggingEndpoint'`

      Examples::

         LOGGING_ENDPOINT_LOGGER = 'MyLogger'

.. py:attribute:: MESSAGE_HANDLER

      Function to process the incoming message by the application.
      Takes the original function and should return a tuple of
      * logger name (or None)
      * loglevel
      * log message
      * args for the log call
      * kwargs for the log call

      def default_handler(log_data):
          """Return the message as is as level INFO on the default logger."""
          return None, INFO, log_data.decode(), tuple(), dict()

      Default
         :code:`logging_endpoint.message_handler.default_handler`

      Examples::

         LOGGING_ENDPOINT_MESSAGE_HANDLER = log_message_handler
         LOGGING_ENDPOINT_MESSAGE_HANDLER = 'path.to.handler'

.. py:attribute:: OVERWRITE_LOGGER

      If set to true an incoming json message will be sent to the logger
      specified under the :code:`logger` key. Otherwise the message is sent to
      the standard logger (see setting :code:`LOGGER`) and the logger value is
      added to the message.

      Default
         :code:`False`

      Examples::

         LOGGING_ENDPOINT_OVERWRITE_LOGGER = False

.. py:attribute:: DECOMPOSE_JSON_LIST

      If set to true an incoming json list will be decomposed into separate
      messages:

      True:
        ["log1", "log2"] =>
          INFO log1
          INFO log2
      False:
        ["log1", "log2"] => INFO ["log1", "log2"]

      Default
         :code:`True`

      Examples::

         LOGGING_ENDPOINT_DECOMPOSE_JSON_LIST = True
