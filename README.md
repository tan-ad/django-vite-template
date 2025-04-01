# django-vite-template

## Setup

### venv and django project

```bash
virtualenv venv
source venv/bin/activate
python -m pip install Django
django-admin startproject django_vite_template
```

### Create a dedicated app for users

```bash
cd django_vite_template
python manage.py startapp users
```

### Prepare for Environment-Specific Settings

```bash
pip install django-environ
```

### Create initial migrations

```bash
# Change AUTH_USER_MODEL based on changes in `users` app
python manage.py makemigrations users
python manage.py makemigrations
# Apply changes to tables in db
python manage.py migrate
```
