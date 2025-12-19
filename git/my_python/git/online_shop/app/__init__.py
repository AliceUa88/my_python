from flask import Flask
import json
import os
import sqlite3
#шукає де лежить проект і будує шляхи до шаблонів і статичних файлів
def create_app():
    base_dir=os.path.abspath(os.path.dirname(__file__)+ '/..') 
    app = Flask(__name__, template_folder=os.path.join(base_dir, 'templates'),
                static_folder=os.path.join(base_dir, 'static'))
    
     #Завнтаження конфігурації з config.json
    config_path = os.path.join(base_dir, 'config.json')
    with open(config_path) as f:
        config = json.load(f)
    app.config.update(config)
    #Шукає шлях до бази даних і налаштовує SQLAlchemy
    db_path = os.path.abspath(os.path.join(base_dir, config['DB_PATH']))
    # налаштовує шлях до папки бази даних, якщо її немає - створює
    db_dir = os.path.dirname(db_path)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from .models import db
    db.init_app(app)
    #Перевіряє і додає відсутні колонки в таблицю products
    _ensure_columns(db_path, 'products', 
                    {'created_at': 'DATETIME', 'updated_at': 'DATETIME' , 'description': 'TEXT'})
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)
    return app
    
    
    
    

def _ensure_columns(sqlite_path, table, columns):
    """Переконується, що в таблиці SQLite є вказані стовпці; якщо їх немає, додайте їх.


    Це оновлює файл SQLite на місці (без резервного копіювання) відповідно до запиту.
    """
    if not os.path.exists(sqlite_path):
        return
    conn = sqlite3.connect(sqlite_path)
    cur = conn.cursor()
    try:
        cur.execute(f"PRAGMA table_info('{table}')")
        existing = {row[1] for row in cur.fetchall()}  # row[1] - назва стовпця, сбирає назви існуючих стовпців
        for col, col_type in columns.items():
            if col not in existing:
                stmt = f"ALTER TABLE {table} ADD COLUMN {col} {col_type};" #додає відсутні колонки
                try:
                    cur.execute(stmt)
                except Exception:
                    # ігноруємо помилки додавання колонки
                    pass
        #Після додавання колонок оновлюємо NULL значення на поточну дату/час
        # Використовуємо try-except щоб уникнути помилок, якщо колонка вже має значення
        try:
            if 'created_at' in columns:
                cur.execute(f"UPDATE {table} SET created_at = CURRENT_TIMESTAMP WHERE created_at IS NULL;")
            if 'updated_at' in columns:
                cur.execute(f"UPDATE {table} SET updated_at = CURRENT_TIMESTAMP WHERE updated_at IS NULL;") #оновлює NULL значення
        except Exception:
            # ігнорує помилки оновлення
            pass
        conn.commit()
    finally:
        cur.close()
        conn.close()
