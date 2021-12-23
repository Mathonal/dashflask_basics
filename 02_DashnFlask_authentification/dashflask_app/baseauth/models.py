from flask_login import UserMixin
from .. import db

from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin,db.Model):
    """User account model."""
    __tablename__ = 'flasklogin-users'

    id = db.Column(db.Integer, primary_key=True) 
    # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__(self, email, name, password):
        self.email = email       
        self.name = name
        #self.password = generate_password_hash(password, method='sha256')
        self.set_password(password)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)    


class UserDashboard(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000))
    dashref = db.Column(db.String(100))

    def __init__(self, name, dashref):
        self.name = name
        self.dashref = dashref


def init_db():
    db.drop_all()
    db.create_all()

    db.session.add(User("test@mail.com", "testname",'dashtest'))
    db.session.add(User("test2@mail.com", "testname2",'dashtest'))

    db.session.add(UserDashboard("testname",'dashtest1'))
    db.session.add(UserDashboard("testname2",'dashtest2'))

    db.session.commit()
    #lg.warning('Database initialized!')
    print('Database initialized!')