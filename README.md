# echoservice

## What is `echoservice`

`echoservice` is a simple webservice which:

* exposes a single enpoint `/humai/echoservice` accepting JSON HTTP POST requests
* itreturns a JSON payload with the request payload and timestamp of the time when the request was received
* stores the payload to an SQLite database
* is written in Python 3
* is a [WSGI](https://wsgi.readthedocs.io/en/latest/index.html) application
* uses [`Flask`](https://flask.palletsprojects.com/en/1.1.x/), [`Flask-SQLAlchemy`](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) and [gunicorn](https://gunicorn.org/)

### Response format

```json
{
    "payload": <request payload>,
    "timestamp": <unix timestamp of the time when the request was received as integer>
}
```

### Example

**Request** sent to `/humai/echoservice` endpoint received at 2020-10-10 13:00:00

```json
{
    "firstName": "John",
    "lastName": "Doe"
}
```

**Response**
```json
{
    "payload": {
        "firstName": "John",
        "lastName": "Doe"
    },
    "timestamp": 1602327600
}
```

## How to run `echoservice`

To run `echoservice` use the prepared docker image.

Get the image run the following command:

```bash
$ docker pull suic/echoservice:v0.1.0
```

Run the `echoservice`:

```bash
$ docker run -d \ 
-p <port_on_your_machine>:8080 \ 
-v "<path_to_local_sqlite_database>:/echoservice/database.sqlite" \
suic/echoservice:v0.1.0
```

#### Example

```bash
# run echoservice on port 5050 and use /tmp/database.sqlite to store the payload
$ docker run -d \
-p 5050:8080 \
-v "/tmp/database.sqlite:/echoservice/database.sqlite" \
suic/echoservice:v0.1.0

# test echoservice with curl
$ curl --header "Content-Type: application/json" \
--request POST \
--data '{"username":"xyz","password":"xyz"}' "http://localhost:5050/humai/echoservice"

# Expected return value. The timestamp will be different.
{"payload":{"password":"xyz","username":"xyz"},"timestamp":1602355857}
```