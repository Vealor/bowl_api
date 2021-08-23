"""
Bowl endpoints

Currently only has 1 endpoint to determine total score from a bowling game
"""
# ==============================================================================
from sanic import Blueprint
from sanic.response import json

from src.models.bowls import Bowl
# ==============================================================================
bowl = Blueprint('bowl', __name__)
# ==============================================================================


@bowl.route('/', methods=['POST', 'OPTIONS'])
async def post_get_score(request):
    """Receives data for a bowling match for 10 frames and gives score


    """
    response = {'status': 'ok', 'message': '', 'payload': []}
    input_data = request.json

    # Bowl.check_valid(input_data)

    response['payload'] = Bowl.get_score(input_data)

    return json(response, status=200)
