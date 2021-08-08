from itertools import product
from flask.helpers import flash
from wtforms.validators import Email
from app import app, db
from flask import render_template, redirect, url_for
from app.forms import Create_product#, LoginForm, RegisterForm
from app.models import CartItem, Product, User
#from flask_login import login_required, login_user, logout_user, current_user, login_manager

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

    return render_template('shop.html',products=my_products)

#aaron edit

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html',products=products)
    
@app.route('/cart/<int:product_id>', methods=['POST', 'GET'])
def add_to_cart(product_id):
    product = Product.query.filter(Product.id == product_id)
    cart_item = CartItem(product=product)
    db.session.add(cart_item)
    db.session.commit()
    return render_template('index.html', product=products)
    
def remove_from_cart(product_id):
    product = Product.query.filter(Product.id == product_id)
    cart_item = CartItem(product=product)
    db.session.remove(cart_item)
    db.session.commit()
    return render_template('index.html', product=products)


def getproductitem():
    itemid = products.id
    productname = products.name
    productname = CartItem(product_id=itemid)
    db.session.add(products)
    db.session.commit()
    return render_template('index.html',products=products)



# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         # Grab data from our submitted form
#         email = form.email.data
#         password = form.password.data
#         print(email, password)
#         # Create new instance of User
#         new_user = User(email, password)

#         # Add new_user to our database
#         db.session.add(new_user)
#         db.session.commit()

#         # Once new_user is added to db, flash success message
#         flash(f'Thank you for signing up {new_user.username}!', 'danger')

#         # Redirect user back to home page
#         return redirect(url_for('index'))
#     return render_template('register.html', title='Register for CT Blog', form=form)

# @login_manager.user_loader
# def load_user(email):
#     return User.get(email)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         email=form.email.data
#         password = form.password.data
#        #return the first user object
#         user = User.query.filter_by(email=email).first()
        
        
#         if user is None or user.check_password(password): 
#             flash('Incorrect Email/Password. Try Again', 'danger')
#             return redirect(url_for('login'))

#         login_user(user)
#         flash('You have successfully logged in!', 'success')
#         return redirect(url_for('index'))
