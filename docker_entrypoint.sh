
# Start Gunicorn processes
echo Starting Gunicorn

# run the created app from run.py
# bind to this port
# how many threads to create
exec gunicorn run:app --name test --bind 0.0.0.0:2626 --worker-class gevent --workers 3
