"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """User."""
    __tablename__ = "users"

    id = db.Column(db.Integer, 
                    primary_key=True, 
                    autoincrement=True)
    first_name = db.Column(db.String(50),
                    nullable=False)
    last_name = db.Column(db.String(50),
                    nullable=False)
    image_url = db.Column(db.String(200),
                    nullable=False,
                    default='https://www.pngkey.com/png/detail/230-2301779_best-classified-apps-default-user-profile.png')

    def get_full_name(self):
        """Returns full name of our user"""
        return f"{self.first_name} {self.last_name}"
