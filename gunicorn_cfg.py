daemon=True
bind='unix:/home/ubuntu/run/gunicorn.sock snudcm.wsgi:application'
workers=5