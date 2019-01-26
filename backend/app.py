from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.

    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

@app.route("/shows", methods=['GET'])
def get_all_shows():
    minEpisodes = 0
    if request.args.get('minEpisodes') is not None:
        minEpisodes = int(request.args.get('minEpisodes'))

    data = [show for show in db.get('shows') if show['episodes_seen'] >= minEpisodes]
    return create_response({"shows": data})

@app.route("/shows", methods=['POST'])
def add_show():
    if "name" not in request.json or "episodes_seen" not in request.json:
        return create_response(status=422, message="Did not provide required information to add show")

    name = request.json["name"]
    episodes_seen = request.json["episodes_seen"]

    payload = db.create('shows', {
        "name": name,
        "episodes_seen": episodes_seen
    })

    return create_response(status=201, data=payload)

@app.route("/shows/<id>", methods=['GET'])
def get_show_with_id(id):
    data = db.getById('shows', int(id))
    if data is None:
        return create_response(status=404, message="No show with this id exists")
    return create_response(data)


@app.route("/shows/<id>", methods=['PUT'])
def put_show_with_id(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    item = db.updateById('shows', int(id), request.json)
    return create_response(status=201, data=item)

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    db.deleteById('shows', int(id))
    return create_response(message="Show deleted")


# TODO: Implement the rest of the API here!

"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
