from unicodedata import name
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
        name = request.form['name']
        price = request.form['price']
        description = request.form.get('description')
        stock = request.form.get('stock', type=int)
        category = request.form.get('category')
        rating = request.form.get('rating', type=float)
        product = Product(
            name=name,
            price=float(price),
            description=description,
            stock=stock or 0,
            is_active='is_active' in request.form, 
            category=category,
            rating=rating or 0.0,
            sale='sale' in request.form  
)
        db.session.add(product)
        db.session.commit()
        flash("Product added")
        return redirect(url_for('routes.product'))
    return render_template('product_form.html', action='Add', product=None)