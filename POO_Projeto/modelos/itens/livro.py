from POO_Projeto.modelos.itens.item_biblioteca import ItemBiblioteca

# Ao colocar como parâmetro a classe ItemBibliotec, estou herdando dela. No Java usamos o "Extends", aqui no Python, basta usar a classe pai dentro do parâmetro da classe filha

class Livro(ItemBiblioteca):
  def __init__(self, titulo, autor, preco, isbn):
    super().__init__(titulo, autor, preco)
    self._isbn = isbn

  def aplicar_desconto(self):
    self._preco -= (self._preco * 0.10) # 10% de desconto