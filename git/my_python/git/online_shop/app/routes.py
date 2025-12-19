from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Product
bp=Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/products')
def product():
    products=Product.query.all()
    return render_template('product_list.html', 
                           products=products)


@bp.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name=request.form['name']
        price=request.form['price']
        product=Product(name=name, price=float(price))
        db.session.add(product)
        db.session.commit()
        flash("Product added")
        return redirect(url_for('routes.product'))
    return render_template('product_form.html', action='Add', product=None)