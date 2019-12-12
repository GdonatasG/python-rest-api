from api import db

class Car(db.Model):
    __tablename__ = 'car'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
    engine = db.Column('engine', db.Unicode)
    gas_type = db.Column('gas_type', db.Unicode)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, name, engine, gas_type):
        self.name = name
        self.engine = engine
        self.gas_type = gas_type

    def __repr__(self):
        return '' % self.id
