from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()
class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True
def __init__(self, *args):
        super().__init__(*args)
def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })
def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }
class User(db.Model):
    __tablename__ = 'customer'
    passenger_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    telephone=db.Column(db.String(80))
    email = db.Column(db.String(80))
    party=db.Column(db.String(80))
    card_number = db.Column(db.String(80))
    flight_no = db.Column(db.String(80))
    boarded = db.Column(db.String(80))
def __init__(self, id, name, telephone, email, party, card_number):
        self.passenger_id = id
        self.name = name
        self.email = email
        self.telephone = telephone
        self.party = party
        self.card_number=card_number