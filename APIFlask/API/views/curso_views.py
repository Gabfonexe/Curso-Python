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
      nome = request.json["nome"]
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
    cs = curso_schema.CursoSchema() #Como queero recuperar somente 1 valor, não passo o many=true
    return make_response(cs.jsonify(curso), 200) # jsonfy para retornar em formato json

  def put(self):
    curso_bd = curso_service.listar_curso_id(id)
    if curso_bd is None:
      return make_response(jsonify("Curso não foi encontrado"), 404)
    cs = curso_schema.CursoSchema() #Como queero recuperar somente 1 valor, não passo o many=true
    validate = cs.validate(request.json) #Verificar a validação dos dados
    if validate: #Caso houver algum erro de validação
      return make_response(jsonify(validate), 400)
    else:
      nome = request.json["node"]
      descricao = request.json["descricao"]
      data_publicacao = request.json["data_publicacao"]
      novo_curso = curso.Curso(name=nome, descricao=descricao, data_publicacao=data_publicacao)
      curso_service.atualiza_curso(curso_bd, novo_curso)
      curso_atualizado = curso_service.listar_curso_id(id)
      return make_response(cs.jsonify(curso_atualizado), 200) # atualizar e ter acesso ao recurso atualizado, por isso coloco esse retorno.


  def delete(self):
    curso_bd =  curso_service.listar_curso_id(id)
    if curso_bd is None:
      return make_response(jsonify("Curso não encontrado"), 404)
    curso_service.remove_curso(curso_bd)
    return make_response('Curso excluído com sucesso', 204)

     
api.add_resource(CursoList, '/cursos') # criando rota default de listas de curso
api.add_resource(CursoDetail, '/cursos/<int:id>') # Criando rota de obter pelo ID