from core.main import bp
from flask import render_template
from datetime import datetime

today = datetime.today()
month = today.strftime("%B")



@bp.route('/')
def index():
    return render_template(
        'index.html',
        title = 'Spendr - Track your spending',
        month = month
    )