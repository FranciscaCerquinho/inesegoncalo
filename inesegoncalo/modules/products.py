from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from inesegoncalo.tools import tools

from inesegoncalo.models import Product , Contribution


bp = Blueprint('products', __name__, url_prefix='/products')

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from inesegoncalo.tools import tools

from inesegoncalo.models import Product, Contribution, Category

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/all', methods=('GET', 'POST'))
@bp.route('/all/<update>', methods=('GET', 'POST'))
@bp.route('/all/category/<category_id>', methods=('GET', 'POST'))
def all(update=None, category_id=None):
    categories = Category.query.all()
    
    # Filtrar produtos por categoria se especificado
    if category_id:
        products = Product.query.filter_by(category_id=category_id).order_by(Product.priority).all()
    else:
        products = Product.query.filter_by().order_by(Product.priority).all()
    
    if update == 'update':
        for product in products:
            product.update_price_paid()
    
    products_paid = [product for product in products if product.is_paid()]
    products = [product for product in products if not product.is_paid()]
    
    return render_template('products/all.html', 
                         products=products, 
                         products_paid=products_paid,
                         categories=categories,
                         selected_category_id=category_id)

@bp.route('/add_contribution', methods=('GET', 'POST'))
def add_contribution():
    return render_template('products/add_contribution.html')

@bp.route('/product/<product_id>', methods=('GET', 'POST'))
@bp.route('/product/<product_id>/<contribution_id>', methods=('GET', 'POST'))
def product(product_id,contribution_id=None):
    product = Product.query.filter_by(id=product_id).first()
    contribution=None
    if contribution_id:
        contribution = Contribution.query.filter_by(id=contribution_id).first()

    ##VERFICAR SE A CONTRIBUICAO FOI DESTE PRODUTO
    if request.method == 'POST':
        error = None
        name = request.form.get('name')
        value_contributed_original = request.form.get('value_to_contribute')
        value_contributed = float(value_contributed_original) if tools.is_float(value_contributed_original) else None
        message = request.form.get('message')

        if not name:
            error = 'Pedimos desculpa, mas precisamos de um nome para poder registar a contribuição'
        if not value_contributed_original:
            error = 'Pedimos desculpa, mas precisamos de um valor para poder registar a contribuição'
        if not value_contributed:
            error = 'Pedimos desculpa, mas o valor precisa de ser escrito só com números'

        if error is None:
            contribution = Contribution(name=name,value_contributed=value_contributed,product_id=product.id)
            if message:
                contribution.message = message
            contribution.create()

            product.price_paid += value_contributed
            product.save()

            return redirect(url_for('products.add_contribution'))

            #return redirect(url_for('products.product',product_id=product.id,contribution_id=contribution.id))
        flash(error)
    return render_template('products/product.html',product=product,contribution=contribution)

@bp.route('/lista_casamento', methods=('GET', 'POST'))
def lista_casamento():
    return render_template('products/lista_casamento.html')

@bp.route('/luademel', methods=('GET', 'POST'))
def luademel() :
    return render_template('products/luademel.html')


@bp.route('/casa', methods=('GET', 'POST'))
def casa() :
    return render_template('products/casa.html')
