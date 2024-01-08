import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@localhost/dbmain'
SQLALCHEMY_TRACK_MODIFICATIONS = False

broker_url = 'pyamqp://guest:guest@localhost//'
result_backend = 'rpc://'
