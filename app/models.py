from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)

    def __repr__(self):
        return f"<Post {self.id}>"