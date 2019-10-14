import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '3R5vOopI1zsdvUdc'
