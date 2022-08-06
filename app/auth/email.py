from flask import render_template, current_app
from flask_mail import Message
from threading import Thread
from app import mail, app

def send_async_email(app, msg):
    # There are two types of contexts, the application context and the request context. 
    # In most cases, these contexts are automatically managed by the framework, but when 
    # the application starts custom threads, contexts for those threads may need to be 
    # manually created.
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))