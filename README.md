# Ami-feedbacker
kurssipalautejärjestelmä

Clone repo
```
$ git clone https://github.com/Samirboudissa1994/Ami-feedbacker.git
```
You need to have a Virtualenv on your computer in order to use this program. If you don't have it, you can install it by typing the following in your terminal:

```
sudo apt-get install python3-venv
```

Create python virtualenv, and activate it and install requirements 
```
$ python3 -m venv venv_feedbacker
$ . venv_feedbacker/bin/activate
$ cd Ami-feedbacker
$ pip install -r requirements.txt
```

Creating a new admin account:

First create a database for the admin user(s):
```
. venv_feedbacker/bin/activate
$ cd Ami-feedbacker
$ python
>>> from app import db
>>> db.create_all
```
The database file should now be visible in your app directory

Next, add a user or users to your database:
```
>>> from app import User
>>> any_variable_name = User(username='name_of_your_user', password='your_password')
>>> db.session.add(variable_name)
*NOTE: you can also add another user by repeating steps 2 and 3 before committing them to your new db*
```
now, commit the changes:
```
>>> db.session.commit()
```
Your admin user(s) should now be stored in your new db and be operable

Checking the users stored in your db:
```
$ python
>>> from app import db
>>> User.query.all()
>>> from app import User
```
Users should now be shown on a list


Run App, use -b switch to bind ip, -b 127.0.0.1:{PORT} listens localhost
```
$ gunicorn -b 0.0.0.0:8080 main:app
```

Build & run docker
```
docker build -t Ami-feedbacker:latest .
docker run --name Ami-fb -d -p 8080:8080 Ami-feedbacker:latest
```

gcp sdk console commands to build and deploy, 
```
$ git clone https://github.com/Samirboudissa1994/Ami-feedbacker.git
$ cd Ami-feedbacker
$ gcloud builds submit --tag gcr.io/Ami-feedbacker/Ami-feedbacker
$ gcloud beta run deploy --image gcr.io/Ami-feedbacker/Ami-feedbacker --platform managed
```
