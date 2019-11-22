from flask import jsonify, Blueprint, request

total_bp = Blueprint('total_bp', __name__)


@total_bp.route('/total', methods=['POST', 'GET'])
def total():
    """
    This endpoint calculates the sum of a given list of numbers. Assuming one wants to try custom input
    there is also a POST method provided.
    methods:
        - GET: when get is called it will compute a hard-coded list of numbers as per specs.
        - POST: when post is called it will compute user provided list from a json body.
    parameters:
        - numbers:
          in: body
          type: json
          required: true
          description: a user provided list of numbers to sum, in the body of a POST request.
    responses:
        - 200:
            description: returns the result of the sum in a json format.
        - 404:
            description: when the request is not found.
        - 400:
            description: when no input or wrong input is passed as the body for the POST request.
        - 500:
            description: when non-json input is passed as the body for the POST request.
    """

    if request.method == 'POST':
        body = request.get_json()
        if request.data and 'numbers' in body.keys():
            return compute_sum(body['numbers'])
        else:
            return "Invalid input!", 400
    else:
        numbers_to_add = list(range(10000001))
        return compute_sum(numbers_to_add)


def compute_sum(numbers):
    return jsonify(total=sum(numbers))
