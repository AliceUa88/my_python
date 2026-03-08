from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(100), nullable=False)
    price=db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    description = db.Column(db.Text, nullable=True)
    stock = db.Column(db.Integer, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    category = db.Column(db.String(100), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    sale = db.Column(db.Boolean, default=False)