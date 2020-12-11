# first-django-app
First Django web application based on https://docs.djangoproject.com/ko/2.0/intro/tutorial01/
It uses python3.6, sqlite3

This Project contains minimal voting app.

## Quick Start

    # Clone repository
    git clone https://github.com/suhyunyoon/first-djagno-app
    
    cd first-django-app
    
    # Migrate django app and Create DB Table
    python3 manage.py migrate
    
    # Start server
    python3 manage.py runserver
    or
    python3 manage.py runserver (ip addr):(port)
    
    # Create admin page account
    python manage.py createsuperuser

## Documentation
### File Structure
`/manage.py` is an executing file.
Static file of admin page is in `/templates/`.
All source code of voting app is in `/polls/`.

### Dependencies
This project uses python3.6, sqlite3.
Also this project generates and uses sqlite db file `db.sqlite3`.

    # Enter sqlite shell
    sqlite3
    
    # Open DB file
    .open db.sqlite3
    
    # Querying anything!
