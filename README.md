# navigation-server

## Introduction
Navigation server provides RESTful services for navigation view front end. 

The services provided include <b>flight search</b> service, <b>navigation</b> service, <b>restuarants look up</b> service and <b>nearby exploration</b> service. 

## Release Notes
### What's New In This Version
* Provide navigation service to front end, which specfies all end points and directions.
* Provide flight search service to front end. Users are able to get flight information, including flight status, departure terminal and gate. 
* Provide restuarants look up services. Users from front end are able to get all restuarants data overview in a specific terminal and also all restuarants details. 

### Konwn Bugs and Defects
* The flight external API is relatively unstable, so the server will be temporarily down sometime. 
* Because our current setup, we have cross-origin issue. 

## Download Project
* Download by using git.

```
git clone https://github.com/GTAirportNavigation/navigation-server.git
```

* Download zip file from GitHub webiste. [zip address](https://github.com/GTAirportNavigation/navigation-server)

## Install Guide
### Pre-requisites

* Python >= 3.6
* pip 
* git

### Dependencies
All other dependent libraries are in the `requirements.txt` file. You can install packages by using `pip`.

* Install other required dependencies.

```
pip install -r requirements.txt
```

* Update all packages to latest versions.

```
pip install -r requirements.txt --upgrade
```

## Run Instructions
* Start local Mysql server

```
mysql.server start
```
or

```
sudo mysql.server start
```

* For Mysql database setup, check `MYSQL_INSTRUCTION.md`.
* Once this is done, run `ahj.sql` to init airport database.
* Do Django backend migration.

```
python manage.py makemigrations
python manage.py migrate
```

* Start the backend server.

```
python manage.py runserver
```

## TroubleShooting
* Database related
	* Make sure you have started Mysql server.
	* You have `GTAirportNavigation` database setup in your Mysql server.
	* Go to `root/settings.py`, change database `username` and `password`.
	* Make sure you run Django migrations successfully.
