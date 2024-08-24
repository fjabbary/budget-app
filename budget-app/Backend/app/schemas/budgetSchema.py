from app.schemas import ma
from marshmallow import fields
from marshmallow import Schema, fields, validate, post_load

class BudgetSchema(Schema):
    monthly_income = fields.Float(required=True, validate=validate.Range(min=0))
    checking_balance = fields.Float(required=True, validate=validate.Range(min=0))
    
    expenses = fields.Dict(keys=fields.Str(), values=fields.Float(), required=True)
    
    @post_load
    def make_budget(self, data, **kwargs):
        return Budget(**data)
