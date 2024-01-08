# app/__init__.py
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate

app = Flask(__name__)

# Load configuration from config.py in the root directory
# app.config.from_pyfile('../config.py')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost/dbmain'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
celery = Celery(
    app.name,
    broker= 'transport://guest:guest@localhost//',
    backend= 'rpc://'
)
celery.conf.update(app.config)

# Rate Limiting
limiter = Limiter(
    get_remote_address,
    app=app,
    # default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

# Import models to create tables
from app import models

# Import views to register the routes
from app import views
