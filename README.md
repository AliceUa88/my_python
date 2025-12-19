# my_python
# Simple Python Online Shop
Онлайн-магазин на Flask, який відображає список товарів із бази даних SQLite.
## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Make sure the `templates` folder exist and are not empty.
3. Start the application:
   ```bash
   python run.py
   ```
4. Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


## Project Structure
- `app/` — Main application code
- `templates/` — HTML-шаблони для відображення сторінок
- `static/` — стилі, скрипти та зображення
- `db/` — SQLite database file
- `config.json` — Configuration parameters
- `run.py` —  запускає flask
