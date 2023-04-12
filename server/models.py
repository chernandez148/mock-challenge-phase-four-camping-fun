from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()


class Camper(db.Model, SerializerMixin):
    __tablename__ = 'campers'

    serialize_rules = ('-activities.campers', '-signups.activity')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    created_at = db.Coulmn(db.DateTime, server_default = db.func.now())
    update_at = db.Column(db.DateTime, onupdate = db.func.now())

    activities = db.relationship('Signup', backref = 'camper')


class Activity(db.Model, SerializerMixin):
    __tablename__ = 'activities'

    serialize_rules = ('-campers.activities', '-signups.camper')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    difficulty = db.Column(db.Integer)
    created_at = db.Coulmn(db.DateTime, server_default = db.func.now())
    update_at = db.Column(db.DateTime, onupdate = db.func.now())

    campers = db.relationship('Signup', backref= 'activity')


class Signup(db.Model, SerializerMixin):
    __tablename__ = 'signups'

    serialize_rules = ('-camper.activities', '-activity.campers')

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer)
    created_at = db.Coulmn(db.DateTime, server_default = db.func.now())
    update_at = db.Column(db.DateTime, onupdate = db.func.now())

    camper_id = db.Column(db.Integer, db.ForeignKey('campers.id'))
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'))

