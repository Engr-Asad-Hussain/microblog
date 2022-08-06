from flask import Blueprint, render_template

bp = Blueprint('errors', __name__)

from app.errors import handlers
