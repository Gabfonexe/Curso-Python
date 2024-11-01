class Game:
  # o self funciona como .this do java e javascript. Ele referencia ao atributo da classe
  def __init__(self, name="", yearLaunch=0 , multiplayer=0, note=0):
    self.name = name
    self.yearLaunch =yearLaunch
    self.multiplayer = multiplayer
    self.note = note

  # Parecido com o metodo toString() do java
  def __str__(self):
    return f'Game: {self.name}'
  


game1 = Game("Fortnite", 2017, True, 8.4)
game2 = Game("Call of Dutty Ghosts", 2014, True, 9.1)




    
