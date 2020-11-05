daemon=True
bind='unix:/home/ubuntu/dwnusa/run/gunicorn.sock news.wsgi:application'
workers=5