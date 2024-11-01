from flask import Flask, render_template, request

# Sempre usar na primeira vez que usar o Flask, esse comando - set FLASK_APP=app.py / Isso configura a variavel de ambiente

# set FLASK_ENV=development = Define o modo de operação para desenvolvimento, com isso é possível notar a mudança do app de forma síncrona

# Sempre que for utilizar o render_template, basta colocar o nome da pasta como "templates", que ele irá reconhecer automaticamente

# Definir o nome do app // instanciando
app = Flask(__name__)

frutas = [] # A lista está no escopo Global

alunos = []  # Nesse caso, precisei criar uma lista para poder adicionar dinamicamente no dicionário


# Criar a rota
@app.route('/', methods=["GET", "POST"]) #Rota principal normalmente é a /
def principal():

  if request.method == "POST":
    if request.form.get("fruta"):
      frutas.append(request.form.get("fruta")) # Após clicar em adicionar fruta no template (front), é chamado essa requisição. O "request.get" irá pegar o que foi digitado no campo form do HTML

  return render_template("index.html", frutas=frutas) # Ao retornar a var nome e idade, consigo acessar ela no arquivo html do parâmetro



@app.route('/sobre', methods=["GET", "POST"])
def adicionarAluno():
  # notas = {"Fulano":5.0, "Beltrano":6.0, "Aluno":7.0, "Sicrano":8.5}

  if request.method == "POST":
    if request.form.get("aluno") and request.form.get("nota"):
      alunos.append({"aluno": request.form.get("aluno"), "nota": request.form.get("nota")})

  return render_template("sobre.html", alunos=alunos)


@app.route('/filmes')
def filmes():
  url = "exemplo"

  resposta = urli


