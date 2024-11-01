from abc import ABC, abstractmethod # Importa a classe abstrata


class ItemBiblioteca(ABC): # Ao passar o "ABC" no parâmetro, tornamos a classe, uma classe abstrata
  def __init__(self, titulo, autor, preco):
    self._titulo = titulo
    self._autor = autor
    self._preco = preco

  
  @abstractmethod
  def aplicar_desconto(self):
    pass
  