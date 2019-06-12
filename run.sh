#!/bin/sh
echo "If this doesn't work, run using . ./run.sh not ./run.sh";
source backenv/bin/activate
cd backend/python
gunicorn -w 1 -b 0.0.0.0:5000 master_wsgi:app --daemon
cd ../../
deactivate
