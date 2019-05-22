from flask_sqlalchemy import SQLAlchemy
import json
# from server import app
from decimal import Decimal
from datetime import datetime


# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class Silver(db.Model):

    __tablename__ = 'silver_metals'

    silver_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Numeric, nullable=False) #Numeric or float


    def __repr__(self):
        """Provide helpful representation when printed."""

        return f'id: {self.silver_id} Date: {self.date} Price: {self.price}'



class Gold(db.Model):

    __tablename__ = 'gold_metals'

    gold_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Numeric, nullable=False) #Numeric or float


    def __repr__(self):
        """Provide helpful representation when printed."""

        return f'id: {self.gold_id} Date: {self.date} Price: {self.price}'

    def get_data(self):

        return {  str(self.date) : self.price}


class DecimalEncoder(json.JSONEncoder):
    ''' this class is used to help serialize numbers with decimal (json cant serialize umbers with Decimal'''
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        if isinstance(o,datetime):
            return o.isoformat()

        return super(DecimalEncoder, self).default(o)    




class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


def example_data():
    """Create some sample data."""

    # In case this is run more than once, empty out existing data
    Gold.query.delete()

    # Add sample employees and departments
    
    a=Gold('2019-05-17 ' , 14.348)
    b=Gold('2019-05-17', 15.348)
    c=Gold('2019-05-17' , 18.348)
    


    db.session.add_all([a,b,c])
    db.session.commit()



def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///goldsilver'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #this helps save resouces if (sqlachemy event system tracks notification)

    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.") 
