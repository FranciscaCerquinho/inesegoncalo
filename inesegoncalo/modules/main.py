from flask import Blueprint, redirect, render_template, request, url_for

from inesegoncalo.models import Product, Hotel, FAQ, HotelReservation

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


@bp.route('/hotel-reserva', methods=('GET', 'POST'))
def hotel_reservation():
    if request.method == 'POST':
        guest_names = request.form.get('guest_names')
        num_rooms = request.form.get('num_rooms') or 1
        num_people = request.form.get('num_people') or 1
        email = request.form.get('email')
        phone = request.form.get('phone')

        reservation = HotelReservation(
            guest_names=guest_names,
            num_rooms=int(num_rooms),
            num_people=int(num_people),
            email=email,
            phone=phone,
        )
        reservation.create()

        return render_template(
            'confirmations/confirmation.html',
            confirmation_title='Pedido de reserva enviado',
            confirmation_message='Recebemos o pedido de reserva de hotel. '
            'Obrigado',
        )

    return render_template('main/hotel_reservation.html')

