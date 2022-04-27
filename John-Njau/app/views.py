from flask import render_template
from app import app


#views
@app.route('/')
def home():
    title="Welcome -- Chukua Grocery"
    return render_template('index.html', title=title)

@app.route('/checkout')
def checkout():
    title="checkout -- Chukua Grocery"
    return render_template('checkout.html', title=title)

@app.route('/products')
def products():
    products = "some of our products"
    return render_template('products.html', title="Products -- Chukua Grocery", products=products)