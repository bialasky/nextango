# Django Backend

This is the backend for our project, built with Django and Django REST Framework.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup

1. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate (macOS)

2. Install required packages:
   pip install django djangorestframework django-cors-headers

3. Create a new Django project and app:
   django-admin startproject backend
   cd backend
   python manage.py startapp api

4. Add 'rest_framework', 'corsheaders', and 'api' to INSTALLED_APPS in backend/settings.py

5. Set up your database:
   python manage.py migrate

6. Create a superuser:
   python manage.py createsuperuser

7. Run the development server:
   python manage.py runserver

The server should now be running on `http://localhost:8000`.
