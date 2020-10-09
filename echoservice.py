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


def _run():
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8080,
        help="Port for the service to run. (default: 8080)",
    )
    args = parser.parse_args()
    app = create_app()
    app.run(host="0.0.0.0", port=args.port, debug=True)


if __name__ == "__main__":
    _run()
