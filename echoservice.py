import logging

from json import dumps
from time import time

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Payload(db.Model):
    __tablename__ = "payload"
    id = db.Column(db.Integer, primary_key=True)
    payload = db.Column(db.String)


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./database.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    db.init_app(app)

    @app.route("/humai/echoservice", methods=["POST"])
    def echoservice():
        timestamp = int(time())
        payload = request.json
        save_payload(dumps(payload))
        return jsonify({"timestamp": timestamp, "payload": payload})

    return app


def save_payload(payload):
    db.session.add(Payload(payload=payload))
    db.session.commit()
