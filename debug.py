from echoservice import create_app

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