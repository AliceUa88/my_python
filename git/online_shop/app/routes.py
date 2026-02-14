from unicodedata import name
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Product
bp=Blueprint('routes', __name__)

@bp.route('/')
def index():
    products=Product.query.all()
    return render_template('index.html', products=products)

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

@bp.route('/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted!')
    return redirect(url_for('routes.product'))

@bp.route('/update/<int:product_id>', methods=['GET', 'POST'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.price = float(request.form['price'])
        product.description = request.form.get('description')
        product.stock = request.form.get('stock', type=int)
        product.is_active = 'is_active' in request.form
        product.category = request.form.get('category')
        product.rating = request.form.get('rating', type=float)
        product.sale = 'sale' in request.form
        db.session.commit()
        flash("Product updated")
        return redirect(url_for('routes.product'))
    return render_template('product_form.html', action='Update', product=product)
