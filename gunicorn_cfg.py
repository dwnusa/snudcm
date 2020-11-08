daemon=True
bind='unix:/home/ubuntu/snudcm/run/gunicorn.sock snudcm.wsgi:application'
workers=5