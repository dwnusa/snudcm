```
sudo apt-get update
sudo apt install python3-pip
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install django~=2.0.0
pip install djangorestframework
pip install freeze
touch .gitignore
echo "venv" >> .gitignore
pip freeze > requirements.txt
git commit -a -m 'initial setup'
git push origin main
```

```
django-admin startproject snudcm
python manage.py startapp dcm_editor
```