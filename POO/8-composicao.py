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


class GameStudio:
  def __init__(self, name=""):
    self.name = name
    self.games = []

  def add_game(self, game):
    self.games.append(game)

  def evaluate_studio_quality(self):
    total_notes = sum(game.note for game in self.games)
    num_games = len(self.games)
    if num_games == 0:
      print(f"O estúdio {self.name} ainda não lançou jogo")
    else:
      average_note = total_notes / num_games
      print(f"Avaliação média dos jogos do estúdio {self.name}: {average_note:.2f}")
  

game1 = Game("Fortnite", 2017, True, 7.9)
game2 = Game("COD", 2020, True, 8.3)
game3 = Game("Valorant", 2020, True, 8.5)

studio = GameStudio("Awesome Games")
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)

studio.evaluate_studio_quality()

for game in studio.games:
  game.technical_sheet()
    