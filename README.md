Mastermind API
==============

## Introduction

Mastermind is a code-breaking game for two players. One player becomes the codemaker, the other the codebreaker. The codemaker chooses a pattern of four color code pegs (duplicates allowed) and the codebreaker tries to guess it, in both order and color.
Each guess is made by placing a row of color code pegs on the decoding board. Once placed, the codemaker provides feedback by placing from zero to four key pegs in the small holes of the row with the guess. A black key peg (small red in the image) is placed for each code peg from the guess which is correct in both color and position. A white key peg indicates the existence of a correct color code peg placed in the wrong position.

Example: Given a code [RED, BLUE, GREEN, RED] when the codebreaker gives a code with [RED, GREEN, RED, YELLOW] the feedback will be: 1 black, 2 whites.

For more information about the game: https://en.wikipedia.org/wiki/Mastermind_(board_game)

## Requirements

The only thing you must have installed in your computer is [docker](https://www.docker.com), [docker-compose](https://docs.docker.com/compose) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

Once you have them installed you just have to type the following command from your computer:

```
$ docker-compose up -d
```

## Install virtualenv

```
$ mkvirtualenv --python=/usr/bin/python3 env
$ pip install -r requirements/local.txt
$ pip install -r requirements/test.txt
```

## Apply DB migrations

```
(env)$ cd mastermind
(env)$ ./manage.py migrate --settings=config.settings.local 
```

## Run application

```
(env)$ ./manage.py runserver --settings=config.settings.local 
```

## HowTo play it

### Create game (given a user request)

```
$ http POST localhost:8000/api/games/ code:='["RED", "BLUE", "GREEN", "RED"]' n_rounds=12

HTTP/1.0 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 143
Content-Type: application/json
Date: Tue, 03 Oct 2017 18:14:51 GMT
Location: http://localhost:8000/api/games/2/
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "code": [
        "RED", 
        "BLUE", 
        "GREEN", 
        "RED"
    ], 
    "ended": false, 
    "id": 2, 
    "n_rounds": 12, 
    "round_count": 0, 
    "url": "http://localhost:8000/api/games/2/", 
    "won": false
}
```

### Return feedback given a code guess

```
$ http POST localhost:8000/api/games/2/rounds code:='["RED", "GREEN", "RED", "YELLOW"]'

HTTP/1.0 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 190
Content-Type: application/json
Date: Tue, 03 Oct 2017 18:17:53 GMT
Location: http://localhost:8000/api/rounds/1/
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "black_pegs": 1, 
    "code": [
        "RED", 
        "GREEN", 
        "RED", 
        "YELLOW"
    ], 
    "ended": false, 
    "game": "http://localhost:8000/api/games/2/", 
    "id": 1, 
    "url": "http://localhost:8000/api/rounds/1/", 
    "white_pegs": 2, 
    "won": false
}
```

### Check game historic
This action should be called with an username with a special role.

```
$ http GET localhost:8000/api/games/

HTTP/1.0 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 337
Content-Type: application/json
Date: Tue, 03 Oct 2017 18:23:47 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "count": 2, 
    "next": null, 
    "previous": null, 
    "results": [
        {
            "code": [
                "RED", 
                "BLUE", 
                "GREEN", 
                "RED"
            ], 
            "ended": false, 
            "id": 1, 
            "n_rounds": 12, 
            "round_count": 0, 
            "url": "http://localhost:8000/api/games/1/", 
            "won": false
        }, 
        {
            "code": [
                "RED", 
                "BLUE", 
                "GREEN", 
                "RED"
            ], 
            "ended": true, 
            "id": 2, 
            "n_rounds": 12, 
            "round_count": 2, 
            "url": "http://localhost:8000/api/games/2/", 
            "won": true
        }
    ]
}

```

### Run tests
```
$ ./manage.py test --settings=config.settings.test
```

## Next steps
I chose docker compose because the idea was to create a new docker-compose.yml with a nginx, uwsgi with this application running and finally this postgres  
