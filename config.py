import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@mysql-db:3306/aws-python-flask-db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PASSWORD_HASH_SALT = "tc#123456"