from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///banco.db", echo=True) # Cria o motor do banco de dados
Base = declarative_base() # Cria a instâncida da classe base para definir as tabelas
Base.metadata.create_all(engine) # Cria as tabelas

class Filme(Base): # herdando da classe Base 
  __tablename__ = "filmes"
  id = Column(Integer, primary_key=True)
  nome = Column(String, nullable=False)
  ano = Column(Integer, nullable=False)
  nota = Column(Float, nullable=False)


# Inserir Dados
def adicionar_filme(nome, ano, nota):
  Session = sessionmaker(bind=engine)
  session = Session()
  filme = Filme(nome=nome, ano=ano, nota=nota)
  session.add(filme)
  session.commit()
  session.close()

adicionar_filme("Mario", 2022, 7.6)
adicionar_filme("Sonic", 2023, 8.1)

# Atualizar dados
def atualizar_filme(id, nome=None, ano=None, nota=None):
  Session = sessionmaker(bind=engine)
  session = Session()
  filme = session.query(Filme).filter_by(id=id).first()
  if filme:
    if nome is not None:
      filme.nome = nome
    if ano is not None:
      filme.ano = ano
    if nota is not None:
      filme.nota = nota
    session.commit()
  session.close()

def excluir_filme(id):
  Session = sessionmaker(bind=engine)
  session = Session()
  filme = session.query(Filme).filter_by(id=id).first()
  if filme:
    session.delete(filme)

  session.commit()
  session.close() 


atualizar_filme(1, "Homem Aranha", 2016, 9.0)
