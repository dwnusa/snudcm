```
sudo passwd
```

```
sudo apt-get update
sudo apt-get install wget tree
sudo apt-get install sqlite3 libsqlite3-dev
sudo apt-get install openssl libssl-dev
sudo apt-get install zlib1g-dev
sudo apt install python3-pip
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install django~=2.0.0
pip install djangorestframework
pip install serializers
pip install gunicorn
pip install freeze
touch .gitignore
echo "venv" >> .gitignore
echo ".idea" >> .gitignore
echo "__pycache__" >> .gitignore
echo "db.sqlite3" >> .gitignore
echo "static" >> .gitignore
pip freeze > requirements.txt
git commit -a -m 'initial setup'
git push origin main
```

```
django-admin startproject snudcm .
python manage.py startapp dcm_editor
echo "STATIC_ROOT = os.path.join(BASE_DIR, 'static/')" >> snudcm/settings.py
```
gunicorn --bind 0.0.0.0:8000 snudcm.wsgi:application
gunicorn --bind unix:/home/ubuntu/run/gunicorn.sock snudcm.wsgi:application
```
```
cp /home/ubuntu/snudcm/gunicorn.service /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn.service
sudo sytstemctl enable gunicorn.service
systemctl status gunicorn.service

```
```
cp /home/ubuntu/snudcm/snudcm.com /etc/nginx/sites-available/snudcm.com
sudo ln -s /etc/nginx/sites-available/snudcm.com /etc/nginx/sites-enabled/snudcm.com
sudo nginx -t
sudo systemctl restart nginx
```
```
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
```
