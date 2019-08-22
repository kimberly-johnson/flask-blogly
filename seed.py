from models import User, Post, db, connect_db
from app import app

connect_db(app)

db.drop_all()
db.create_all()

Posts.query.delete()

whiskey = Post(title='Whiskey', content='Lane', user_id=9)

db.session.add(whiskey)

db.session.commit()