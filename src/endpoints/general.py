'''
General Endpoints
'''
from sanic import Blueprint
from sanic.exceptions import (
    InvalidUsage,  # 400
    Unauthorized,  # 401
    Forbidden,  # 403
    NotFound,  # 404
    RequestTimeout,  # 408
    PayloadTooLarge,  # 413
    HeaderExpectationFailed,  # 417
    ServerError,  # 500
    ServiceUnavailable,  # 503
)
from sanic.response import json
# ==============================================================================
general = Blueprint('general', __name__)
# ==============================================================================


@general.route('', methods=['GET'])
async def default(request):
    """general version endpoint"""
    response = {'status': 'ok', 'message': '', 'payload': []}

    test_code = request.args.get('test', None)
    if test_code == '400': raise InvalidUsage('TEST')  # noqa: E701
    if test_code == '401': raise Unauthorized('TEST')  # noqa: E701
    if test_code == '403': raise Forbidden('TEST')  # noqa: E701
    if test_code == '404': raise NotFound('TEST')  # noqa: E701
    if test_code == '408': raise RequestTimeout('TEST')  # noqa: E701
    if test_code == '413': raise PayloadTooLarge('TEST')  # noqa: E701
    if test_code == '417': raise HeaderExpectationFailed('TEST')  # noqa: E701
    if test_code == '500': raise ServerError('TEST')  # noqa: E701
    if test_code == '503': raise ServiceUnavailable('TEST')  # noqa: E701
    if test_code == 'other': raise ZeroDivisionError('TEST')  # noqa: E701

    response['VERSION'] = request.app.config.VERSION
    response['payload'] = []

    return json(response, status=200)
