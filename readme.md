# Product Management for Zebrands

## Instalation

### Requirements

To run this project you need to install these dependencies:

- Python
- Pip
- Django
- PosgreSQL

#### Create database

You will need to create a posgres database and go to the `settings.py` and edit database info with your credentials

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'product_management',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost'
    }
}
```

Then you will need to run migrations `python manage.py migrate`

#### Edit the file .env.example to .env with your smtp accounts

`USER_MAIL_PASSWORD = "Here you must enter the password of the smtp account to use"`

#### Create superuser

Go to the console and run `python manage.py createsuperuser`

#### Install dependencies

```
$ pip install psycopg2
$ pip install django-crispy-forms
$ pip install python-decouple
```

### Run project

`python manage.py runserver`
