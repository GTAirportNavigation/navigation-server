# navigation-server

## Introduction
Navigation server provides RESTful services for navigation view front end. 

The services provided include <b>flight search</b> service, <b>navigation</b> service, <b>restuarants look up</b> service and <b>nearby exploration</b> service. 

## Installation
* Dependency

<b>Python >= 3.6</b>

* Install other required dependencies.

```
pip install -r requirements.txt
```

* Update all packages to latest versions.

```
pip install -r requirements.txt --upgrade
```


## Start Server
* For Mysql database setup, check `MYSQL_INSTRUCTION.md`.

* Once this is done, run `ahj.sql` to init airport database.

* Do Django backend migration.

```
python manage.py makemigrations
python manage.py migrate
```

* Start Django server.

```
python manage.py runserver
```
