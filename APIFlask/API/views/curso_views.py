from flask_restful import Resource
from api import api

class CursoList(Resource):
  def get(self):
    return "Estudando API com Flaskdfd"
  
  def post(self):
    cs = curso_schema.CursoSchema()
    validate = cs
  
api.add_resource(CursoList, '/cursos') # criando rota