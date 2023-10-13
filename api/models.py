import enum
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ConservationStatus(enum.Enum):
    extinct = 0
    endagered = 1
    threatened = 2
    near_treatened = 3
    observed = 4
    accepted = 5

class Reptile(db.Model):
    __tablename__ =  'reptiles' 
    
    id = db.Column(db.Integer, primary_key = True) 
    common_name = db.Column(db.String(255)) 
    scientific_name = db.Column(db.String(255))
    native_habitat = db.Column(db.String(255))
    fun_fact = db.Column(db.Text())
    conservation_status = db.Column(db.Enum(ConservationStatus))

    