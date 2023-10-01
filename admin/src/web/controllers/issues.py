from flask import render_template
from src.core import board
from flask import Blueprint

issues_bp = Blueprint('issues', __name__, url_prefix='/consultas')

@issues_bp.get('/')
def index():
    issues = board.list_issues()

    return render_template('issues/index.html', issues=issues)
