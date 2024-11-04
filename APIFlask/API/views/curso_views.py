from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from flask import request, make_response, jsonify
from ..entidades import curso
from ..services import curso_service

class CursoList(Resource):
  def get(self):
    cursos = curso_service.listar_cursos()
    cs = curso_schema.CursoSchema(many=True)
    return make_response(cs.jsonify(curso), 200)
  
  def post(self):
    cs = curso_schema.CursoSchema()
    validate = cs.validate(request.json)
    if validate: # Caso dê erro
      return make_response(jsonify(validate), 400)
    else: # Caso funcione e passe, será criado, gerando um código
      nome = request.json["node"]
      descricao = request.json["descricao"]
      data_publicacao = request.json["data_publicacao"]

      novo_curso = curso.Curso(nome=nome, descricao=descricao, data_publicacao=data_publicacao)
      resultado = curso_service.cadastrar_curso(novo_curso)
      x = cs.jsonify(resultado)
      return make_response(x, 201)
    
class CursoDetail(Resource): #Ao extender da classe Resource, os métodos HTTP serão declarados abaixo

  def get(self):
    curso = curso_service.listar_curso_id(id)
    if curso is None:
      return make_response(jsonify("Curso não foi encontrado"), 404)
    cs = curso_schema.CursoSchema()
    return make_response(cs.jsonify(curso), 200) # jsonfy para retornar em formato json

  def put(self):
    pass

  def delete(self):
    pass

     
api.add_resource(CursoList, '/cursos') # criando rota default de listas de curso
api.add_resource(CursoDetail, '/cursos/<int:id>') # Criando rota de obter pelo ID