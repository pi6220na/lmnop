# Live Music Notes, Opinions and Pictures - API
## lmnop is a spin-off application from https://github.com/LincT/lmn

This MCTC Capstone Project 5 is an API with the following functionality:

* Get local Artists, Venues, and Shows musical events data via a webscrapping technique
* Create JSON files for each table type (e.g. artist, venue, shows (plus notes and users for development testing) and load into database)
* Load JSON files into Database which will be accessed by the API to return records to the main lmn project App
* Listen for API calls from lmn project (via HTTP Restful call) to return requested data
* Note: webscrapping will be done on a schedule performed by a cron job - due to cost on Heroku this may not happen - TBD

### To install

1. Create and activate a virtual environment. Use Python3 as the interpreter. Suggest locating the venv/ directory outside of the code directory.

2. pip install -r requirements.txt

3. python manage.py makemigrations api         (note the 'api' at the end is important - it looks for the api preface in the JSON)

4. python manage.py migrate

5. python manage.py runserver

Site at

127.0.0.1:8000

### Create superuser

`python manage.py createsuperuser`

enter username and password

will be able to use these to log into admin console at

127.0.0.1:8000/admin

# See Test Info Below

### For deployment on Heroku, the settings.py file DATABASE section has been modified changing the name, user, and host to Heroku values. Comment out the Heroku lines and uncomment the local use lines to run on local machine.

### Or

### Comment out Postgres DB and uncomment SQLite DB - much more expedient way to development test

### Optional, if wanting to install and use with local postgresql

A local PostgreSQL server will be faster than a GCP one.
https://github.com/DjangoGirls/tutorial-extensions/tree/master/en/optional_postgresql_installation

Set admin password, remember it.

Start postgres running

`su postgres ` if on a mac/linux
`pg_ctl start`  enter username and password

start postgres shell with `psql`

And create a user called lmnop

```
create user lmnop with password 'password_here';
```

create a database lmnop

create database owner lmnop;


Various postgres shell commands
connect to lmnop database

```
\c lmnop
```

`\dt`    shows tables

`\d table_name`   shows info (and constraints) for a table
other sql as expected

postgres shell command cheatsheet - https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546

set environment variable called
POSTGRES_LMNOP_USER_PASSWORD
with a value of the lmnop user's password


Mac users may need to run these commands; these one time

```
sudo ln -s /Library/PosgreSQL/9.5/lib/libssl.1.0.0.dylib /usr/local/lib
sudo ln -s /Library/PosgreSQL/9.5/lib/libcrypto.1.0.0.dylib /usr/local/lib`
```

And this when you start a new shell; or set it permanently in .bash_profile
`export DYLD_FALLBACK_LIBRARY_PATH=/Library/PostgreSQL/9.5/lib:$DYLD_LIBRARY_PATH`


### Run tests

TBD

### Functional Tests with Selenium

TBD

### Test coverage

TBD

