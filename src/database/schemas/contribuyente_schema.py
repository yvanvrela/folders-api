from extensions.database_extension import ma


class ContribuyenteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'ruc')
