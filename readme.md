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
git push origin main
```

```
django-admin startproject snudcm .
python manage.py startapp dcm_editor
echo "STATIC_ROOT = os.path.join(BASE_DIR, 'static/')" >> snudcm/settings.py
```