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
    try:
        args = parser.parse_args()
        app = create_app()
        app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DEBUG_DB}"
        db.create_all(app=app)
        app.run(host="0.0.0.0", port=args.port, debug=True)
    finally:
        try:
            remove(DEBUG_DB)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    _run()
