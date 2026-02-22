from app import create_app
from app.models import db
from flask import Flask #створює вебсервер для сайту
import os

app = create_app()

if __name__ == "__main__":
    #create DB tables if not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True) #дуже детально виводить помилки323234444