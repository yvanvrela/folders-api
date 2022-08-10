from extensions.database_extension import ma


class FolderShema(ma.Schema):
    class Meta:
        fields = ('id', 'contribuyente_id', 'color', 'time')
