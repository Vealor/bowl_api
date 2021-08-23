"""
Error Handling
"""
# ==============================================================================
from sanic.exceptions import (
    InvalidUsage,  # 400
    Unauthorized,  # 401
    Forbidden,  # 403
    NotFound,  # 404
    MethodNotSupported,  # 405
    RequestTimeout,  # 408
    PayloadTooLarge,  # 413
    ContentRangeError,  # 416
    HeaderExpectationFailed,  # 417
    ServerError,  # 500
    ServiceUnavailable,  # 503
)
from sanic.handlers import ErrorHandler
from sanic.response import json
# ==============================================================================


def apply_error_handler(api):
    class GlobalErrorHandler(ErrorHandler):
        def default(self, request, exception):

            # grab application exceptions
            if isinstance(exception, (
                InvalidUsage,  # 400
                Unauthorized,  # 401
                Forbidden,  # 403
                NotFound,  # 404
                MethodNotSupported,  # 405
                RequestTimeout,  # 408
                PayloadTooLarge,  # 413
                ContentRangeError,  # 416
                HeaderExpectationFailed,  # 417
                ServerError,  # 500
                ServiceUnavailable  # 503
            )):
                status = exception.status_code
            else:
                status = 500

            return json({
                'status': 'error',
                'payload': [],
                'message': exception.args[0]
            }, status=status)

    handler = GlobalErrorHandler()
    api.error_handler = handler  # NOTE: disable this line to show application failures during dev
