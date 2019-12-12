from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from models.Car import Car
from api import db


class CarSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Car
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    engine = fields.String(required=True)
    gas_type = fields.String(required=True)
