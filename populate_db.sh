# !/usr/bin/sh
source backenv/bin/activate
cd backend/python
python -m flask_app.scripts.populate_db
cd ../../
deactivate
