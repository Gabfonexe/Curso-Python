from API import ma
from ..models import curso_model
from marshmallow import fields

class CursoSchema(ma.SQLAlchemyAutoSchema):
  model = curso_model.Curso
  load_instance = True
  fields = ("id", "nome", "descricao", "data-publicacao")

# O ID não precisa pois ele é gerado automaticamente através do autoincremento 
  nome = fields.String(required=True)
  descricao = fields.String(required=True)
  data_publicacao = fields.Date(required=True)