import os
import unidecode

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    url_for,
    current_app,
)
from werkzeug.security import check_password_hash, generate_password_hash
from inesegoncalo.tools import tools

from inesegoncalo.models import Product, ProductImage, Hotel, FAQ, HotelImage, Category, CategoryImage

bp = Blueprint("create", __name__, url_prefix="/create")

@bp.route("/product", methods=("GET", "POST"))
def product():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        price = float(request.form.get("price")) if request.form.get("price") else None
        store = request.form.get("store")
        show_price = True if request.form.get("show_price") else False
        priority = (
            int(request.form.get("priority")) if request.form.get("priority") else None
        )
        category_id = (
            int(request.form.get("category_id")) if request.form.get("category_id") else None
        )

        product = Product(name=name, price=price, show_price=show_price)
        if description:
            product.description = description
        if store:
            product.store = store
        if priority:
            product.priority = priority
        if category_id:
            product.category_id = category_id
        product.create()

        # ... resto do código de imagens permanece igual ...
        
    categories = Category.query.all()
    return render_template("create/product.html", categories=categories)

@bp.route("/hotel", methods=("GET", "POST"))
def hotel():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        phone = request.form.get("phone")
        link = request.form.get("link")

        hotel = Hotel(name=name)
        if description:
            hotel.description = description
        if phone:
            hotel.phone = phone
        if link:
            hotel.link = link
        hotel.create()

        files = request.files.getlist("pictures")

        for index, file in enumerate(files):
            if file.filename:
                # Normalizar o nome da imagem
                image_name = unidecode.unidecode(
                    str(hotel.name).replace(" ", "").lower()
                )
                image_filename = f"{image_name}{index}.jpg"

                # Criar diretório se não existir
                image_folder = os.path.join(
                    current_app.static_folder, "images", "hotels"
                )
                os.makedirs(image_folder, exist_ok=True)

                # Definir caminho completo do arquivo
                path = os.path.join(image_folder, image_filename)

                # Salvar imagem
                file.save(path)

                # Criar e associar a imagem ao produto
                relative_path = os.path.join("images", "hotels", image_filename)
                new_image = HotelImage(path=relative_path.replace("/", "/"))
                new_image.hotel = hotel
                new_image.create()  # Salvar no banco de dados


        return redirect(url_for("edit.hotels"))

    return render_template("create/hotel.html")


@bp.route("/faq", methods=("GET", "POST"))
def faq():
    if request.method == "POST":
        question = request.form.get("question")
        answer = request.form.get("answer")

        faq = FAQ(question=question, answer=answer)
        faq.create()

        return redirect(url_for("edit.faqs"))
    return render_template("create/faq.html")



@bp.route("/category", methods=("GET", "POST"))
def category():
    if request.method == "POST":
        name = request.form.get("name")
        
        if name:
            category = Category(name=name)
            category.create()

            files = request.files.getlist("pictures")

            for index, file in enumerate(files):
                if file.filename:
                    # Normalizar o nome da imagem
                    image_name = unidecode.unidecode(
                        str(category.name).replace(" ", "").lower()
                    )
                    image_filename = f"{image_name}{index}.jpg"

                    # Criar diretório se não existir
                    image_folder = os.path.join(
                        current_app.static_folder, "images", "categories"
                    )
                    os.makedirs(image_folder, exist_ok=True)

                    # Definir caminho completo do arquivo
                    path = os.path.join(image_folder, image_filename)

                    # Salvar imagem
                    file.save(path)

                    # Criar e associar a imagem à categoria
                    relative_path = os.path.join("images", "categories", image_filename)
                    new_image = CategoryImage(path=relative_path.replace("/", "/"))
                    new_image.category = category
                    new_image.create()  # Salvar no banco de dados
            
            return redirect(url_for("edit.categories"))
    
    return render_template("create/category.html")