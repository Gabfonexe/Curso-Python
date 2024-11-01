from flask import Flask

# Sempre usar na primeira vez que usar o Flask, esse comando - set FLASK_APP=app.py / Isso configura a variavel de ambiente


# set FLASK_ENV=development = Define o modo de operação para desenvolvimento, com isso é possível notar a mudança do app de forma síncrona

# Definir o nome do app // instanciando
app = Flask(__name__)

# Criar a rota
@app.route('/') #Rota principal normalmente é a /
def principal():
  return "Hello World"

