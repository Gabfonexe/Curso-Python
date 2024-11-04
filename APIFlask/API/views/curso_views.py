from flask_restful import Resource
from API import api
from ..schemas import curso_schema
from flask import request, make_response, jsonify
from ..entidades import curso
from ..services import curso_service

class CursoList(Resource):
  def get(self):
    return "Estudando API com Flaskdfd"
  
  def post(self):
    cs = curso_schema.CursoSchema()
    validate = cs.validate(request.json)
    if validate:
      return make_response(jsonify(validate), 400)
    
  
api.add_resource(CursoList, '/cursos') # criando rota