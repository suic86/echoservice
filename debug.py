#!/usr/bin/env python3
"""debug.py creates a debug server for development.

It runs echoservice with Flask development server in debug mode.

..code-block:: bash
    # to run
    $ python3 debug.py
    # to get help
    $ python3 debug.py -h
"""
from os import remove
from echoservice import create_app, db

DEBUG_DB = "./debug_database.sqlite"


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
    parser.add_argument(
        "-d",
        "--db-path",
        type=str,
        default=DEBUG_DB,
        help=f"Path to debug database. (default: {DEBUG_DB})",
    )
    try:
        args = parser.parse_args()
        app = create_app()
        app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{args.db_path}"
        db.create_all(app=app)
        app.run(host="0.0.0.0", port=args.port, debug=True)
    finally:
        try:
            remove(DEBUG_DB)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    _run()
