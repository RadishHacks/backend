cd backend/python
gunicorn -w 1 -b 0.0.0.0:5000 master_wsgi:app
python -m flask_app.scripts.populate_db.py
cd ../../
