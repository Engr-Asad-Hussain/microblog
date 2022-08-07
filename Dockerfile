FROM python:slim

RUN useradd microblog

WORKDIR /home/microblog

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP microblog.py

# The chown command allows you to change the user and/or group ownership of a given file/directory.
# Use the ls -l command to find out who owns a file or what group the file belongs to:
# ls -l boot.sh (with user set, you will see root root, which means owner and group are root user) 
# chown USER:GROUP FILE used to change the ownership of a user
# To recursively operate on all files and directories under the given directory, use the -R (--recursive) option:
# Syntax chown -R USER:GROUP DIRECTORY
# Reference: https://linuxize.com/post/linux-chown-command/
# Use docker inspect or vs code extension to see the docker config user
RUN chown -R microblog:microblog ./
USER microblog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]