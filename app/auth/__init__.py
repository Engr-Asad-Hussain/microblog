from flask import Blueprint, render_template

bp = Blueprint('auth', __name__)

from app.auth import routes