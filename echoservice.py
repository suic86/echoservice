from time import time
from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)

    @app.route("/humai/echoservice", methods=["POST"])
    def echoservice():
        timestamp = int(time())
        payload = request.json
        return jsonify({"timestamp": timestamp, "payload": payload})

    return app
