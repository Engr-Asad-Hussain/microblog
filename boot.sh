#!/bin/bash
source venv/bin/activate
flask db upgrade
flask translate compile

exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app

# The parameters are pretty much self-explanatory: We are telling Gunicorn that we want to 
# spawn two worker processes running two threads each. We are also accepting connections 
# from the outside and overriding Gunicorn’s default port (8000).
# gunicorn --chdir app app:app -w 2 --threads 2 -b 0.0.0.0:80

# gunicorn --bind 0.0.0.0:5000 manage:app
# ├── .env.dev
# ├── .env.prod

# gunicorn --workers=2 test:app

# --workers=WORKERS - The number of worker processes. This number should generally be between 2-4 workers per core in the server.
# --bind=BIND  - Specify a server socket to bind. Server sockets can be any of $(HOST),

# https://gunicorn.org/
# https://docs.gunicorn.org/en/stable/run.html
# https://docs.gunicorn.org/en/stable/faq.html#faq
# https://github.com/rakyll/hey