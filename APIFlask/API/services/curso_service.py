from ..models import curso_model
from API import db

def cadastrar_curso(curso):
  curso_bd = curso_model.Curso(nome=curso.model, descricao=curso.descricao, data_publicacao=curso.data_publicacao)
  db.session.add(curso_bd)
  db.session.commit() # realizar as att no BD
  return curso_bd

def listar_cursos():
  cursos = curso_model.Curso.query.all()
  return cursos
