from flask import Flask, jsonify, request
import json

from constants import CATEGORIES

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/")
def index():
    x = request.args.get("x", default=None, type=str)
    y = request.args.get('y', default=None, type=str)
    z = request.args.get('z', default=None, type=str)

    if None in [x, y, z]:
        return jsonify({"status": "error",
                        "message": "X, Y, X params must be included in URL"})

    # Category validation
    if not categories_exist(x, y, z):
        return jsonify({"status": "error",
                        "message": "Category does no exist"})

    data = []

    with open('data/data.json') as json_file:
        followers = json.load(json_file)
        for follower in followers:
            result = {"username": follower["username"],
                      "x": follower[x.lower()],
                      "y": follower[y.lower()],
                      "z": follower[z.lower()]}
            data.append(result)

    return jsonify(data)


def categories_exist(x, y, z):
    """
    Checks to see if categories passed in are valid
    """

    if x.lower() in CATEGORIES and y.lower() in CATEGORIES and z.lower() in CATEGORIES:
        return True
    else:
        return False
