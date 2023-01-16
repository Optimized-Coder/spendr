from core.main import bp
from flask import render_template, redirect, url_for
from datetime import datetime

today = datetime.today()
month = today.strftime("%B")

@bp.route('/')
def index():
    return redirect(
        url_for('main.app', month=month)
    )

@bp.route('/<string:month>/')
def app(month):
    return render_template(
        'index.html',
        title = 'Spendr - Track your spending',
        month = month
    )