from app import db

class Post(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    content = db.Column(db.Text)
