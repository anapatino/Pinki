#####create virtual environment
python -m virtualenv venv
.\venv\Scripts\activate
#####install frameworks
pip install flask flask-cors psycopg2 python-decouple python-dotenv
python .\src\app.py
