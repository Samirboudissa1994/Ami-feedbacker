# Ami-feedbacker
kurssipalautejärjestelmä

Clone repo
```
$ git clone https://github.com/Samirboudissa1994/Ami-feedbacker.git
```

Create python virtualenv, and activate it and install requirements 
```
$ python3 -m venv venv_feedbacker
$ . venv_feedbacker/bin/activate
$ cd Ami-feedbacker
$ pip install -r requirements.txt
```

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
