from models import User, db, connect_db
from app import app

connect_db(app)

db.drop_all()
db.create_all()

# User.query.delete()

# whiskey = User(first_name='Whiskey', last_name='Lane', image_url='https://www.pngkey.com/png/detail/230-2301779_best-classified-apps-default-user-profile.png'

# db.session.add(whiskey)

# db.session.commit()