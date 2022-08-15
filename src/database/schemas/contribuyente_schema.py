from extensions.database_extension import ma
from marshmallow import fields, ValidationError


class ContribuyenteSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    ruc = fields.String(required=True)

    class Meta:
        fields = ('id', 'name', 'ruc')
