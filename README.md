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

### Check if django is working

```bash
# in backend directory
python manage.py check
python manage.py runserver
```

### Create the Vite/Vue Project

```bash
npm create vite@latest frontend -- --template vue
cd frontend
npm install
npm run dev
```

### Install packages for Development Integration

```bash
pip install django-cors-headers django-vite
```

### Install Vue Router

```bash
cd frontend
npm install vue-router@4 # Use @4 for Vue 3
```

### Create API app

```bash
cd backend
python manage.py startapp api
```

## Development workflow

### Backend

```bash
cd django_vite_template # Navigate to Django project root
source ../venv/bin/activate # Activate venv
python manage.py runserver # Runs on http://127.0.0.1:8000
```

### Frontend

```bash
cd frontend # Navigate to Vue project root
npm run dev # Runs on http://localhost:5173
```
