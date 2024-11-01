from flask import Flask, render_template, request
import urllib.request, json

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

  resposta = urllib.request.urlopen(url) # Cria um obj (instância) que acessa a URL desejada

  dados = resposta.read() # Realiza a leitura dos dados da url que está sendo acessada

  jsondata = json.loads(dados) # carrega / transforma os dados em tipo json 

  # return(jsondata['results']) # Retorna somente a camada "results" do arquivo json, ou seja, estou especificando qual parte do json quero receber no momento.

  return render_template("filmes.html", filmes=jsondata['results'])


# Criação de Rota Dinâmica no Flask
@app.route('/filmes/<propriedades>')
def filmes():
  url = "exemplo"

  resposta = urllib.request.urlopen(url) 

  dados = resposta.read() 

  jsondata = json.loads(dados) 

  return render_template("filmes.html", filmes=jsondata['results'])






# Desse modo, garanto que o código irá funcionar sem precisar utilizar o flask run, ele estará de forma dinâmica, atualizando automaticamente
if __name__ == "__main__": 
  app.run(debug=True)
