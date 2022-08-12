from extensions.database_extension import ma
from marshmallow import Schema, fields, validate, ValidationError


class FolderShema(ma.Schema):
    id = fields.Integer()
    contribuyente_id = fields.Integer(required=True)
    color = fields.String(required=True)
    time = fields.String(required=True)

    class Meta:
        fields = ('id', 'contribuyente_id', 'color', 'time')
