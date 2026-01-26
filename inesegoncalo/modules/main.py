from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from inesegoncalo.models import Product , Hotel, FAQ

bp = Blueprint('main', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    hotels = Hotel.query.all()
    return render_template('main/index.html',hotels=hotels)

@bp.route('/faqs', methods=('GET', 'POST'))
def faqs():
    q_and_as = FAQ.query.all()
    return render_template('main/faqs.html',q_and_as=q_and_as)

@bp.route('/personalize', methods=('GET', 'POST'))
def personalize():
    return render_template('main/personalize.html')

@bp.route('/info', methods=('GET', 'POST'))
def info():
    return render_template('main/info.html')    


@bp.route('/hotels', methods=('GET', 'POST'))
def hotels():
    hotels = Hotel.query.all()
    return render_template('main/hotels.html',hotels=hotels)    

