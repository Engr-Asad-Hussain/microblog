from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    """ The app.shell_context_processor decorator registers the function as a shell 
    context function. When the flask shell command runs, it will invoke this function
    and register the items returned by it in the shell session."""
    return { 'db': db, 'User': User, 'Post': Post }

"""
Python Flask SERVER_NAME in app instance.
We had a discussion about the SERVER_NAME in flask app.run(host='') command.
I have observed that,

- When you do not specify SERVER_NAME, it takes default None value. It means that you 
specify app.run(host=None) command. Now, what happens when you do like this? The answer is, 
when you create a container from Dockerfile, and do a quick Postman hit at health_check, 
you will observed that the hits are not getting into your flask application even specifying 
the -p flag in the docker run command.

- On the other hand, if you specify SERVER_NAME='0.0.0.0' you will observed that your docker 
container will now receiving hits from the outside.
"""