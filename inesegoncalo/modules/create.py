import os
import unidecode

from flask import Blueprint, flash, g, redirect, render_template, request, url_for , current_app
from werkzeug.security import check_password_hash, generate_password_hash
from inesegoncalo.tools import tools

from inesegoncalo.models import Product , ProductImage , Hotel , FAQ

bp = Blueprint('create', __name__, url_prefix='/create')

@bp.route('/product', methods=('GET', 'POST'))
def product():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = float(request.form.get('price')) if request.form.get('price') else None
        store = request.form.get('store')
        show_price = True if request.form.get('show_price') else False
        priority = int(request.form.get('priority')) if request.form.get('priority') else None

        product = Product(name=name,price=price,show_price=show_price)
        if description:
            product.description = description
        if store:
            product.store = store
        if priority:
            product.priority = priority
        product.create()

        files = request.files.getlist('pictures')

        for index in range(len(files)):
            file = files[index]
            if file.filename != '':
                image_name = str(product.name).replace(" ", "").lower()
                image_name = unidecode.unidecode(image_name)

                filename = os.path.join('images','products','{image_name}{index}.jpg'.format(image_name=image_name,index=index))
                path = current_app.root_path + url_for('static', filename = filename)
                file_exists = os.path.exists(path)
                if not file_exists:
                    img_file = open(path,'wb')
                    img_file.close()
                file.save(path)

                new_image = ProductImage(path=filename)

                new_image.product = product
                new_image.create()
        return redirect(url_for('edit.products'))


    return render_template('create/product.html')

@bp.route('/hotel', methods=('GET', 'POST'))
def hotel():
    if request.method == 'POST':
        name = request.form.get('name')
        adress = request.form.get('adress')
        phone = request.form.get('phone')
        email = request.form.get('email')

        hotel = Hotel(name=name)
        if adress:
            hotel.adress = adress
        if phone:
            hotel.phone = phone
        if email:
            hotel.email = email
        hotel.create()

        return redirect(url_for('edit.hotels'))


    return render_template('create/hotel.html')

@bp.route('/faq', methods=('GET', 'POST'))
def faq():
    if request.method == 'POST':
        question = request.form.get('question')
        answer = request.form.get('answer')

        faq = FAQ(question=question,answer=answer)
        faq.create()

        return redirect(url_for('edit.faqs'))
    return render_template('create/faq.html')