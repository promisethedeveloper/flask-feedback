from models import db, User, Feedback
from app import app

# Create all tables
db.drop_all()
db.create_all()

User.query.delete()
Feedback.query.delete()






# db.session.add_all([d1, d2, d3, d4, e1, e2, e3, e4, e5, e6, e7, e8])
# db.session.commit()