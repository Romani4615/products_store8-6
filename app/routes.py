from app import app, db
from flask import render_template, redirect, url_for
from app.forms import Create_product
from app.models import Product


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/create_product', methods = ['GET','POST'])
def create_product():
    form = Create_product()
    if form.validate_on_submit():
        product_name= form.product_name.data
        price= form.price.data
        image= form.image.data

        new_product= Product(product_name,price,image)

        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for('home_page'))


    return render_template('create_product.html',hello=form)

@app.route('/products')
def products():
    my_products=Product.query.all()

    return render_template('products.html',products=my_products)