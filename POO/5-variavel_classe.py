# Serve para instanciar uma nova classe através de um método construtor

class Game:
  # o self funciona como .this do java e javascript. Ele referencia ao atributo da classe
  total_games = 0 #Variável de classe para contar o número total de jogos
  def __init__(self, name="", yearLaunch=0 , multiplayer=0, note=0):
    self.name = name
    self.yearLaunch =yearLaunch
    self.multiplayer = multiplayer
    self.note = note
    Game.total_games += 1 # Faz um controle de quantidade de jogos 
    self.totalEvaluation = 0 # Não necessariamente precise passar no parametro todos os atributos
    self.evaluators = 0

  # Parecido com o metodo toString() do java
  def __str__(self):
    return f'Game: {self.name}'
  

  def technical_sheet(self):
    print("###Dados do jogo###")
    print(f"Nome do jogo: {self.name}")
    print(f"Ano de Lançamento: {self.yearLaunch}")
    print(f"Modo multiplayer?  {self.multiplayer}")
    print(f"Avaliação do jogo: {self.note}\n")

  def evaluate(self, note):
    self.totalEvaluation += note
    self.evaluators += 1

  def average(self):
    print(f"Média do filme {self.name}: {self.totalEvaluation / self.evaluators}")