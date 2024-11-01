from POO_Projeto.modelos.Avaliacao import Avaliacao
from POO_Projeto.modelos.itens.item_biblioteca import ItemBiblioteca

class Biblioteca:
  bibliotecas = []

  def __init__(self, nome):
    self.nome = nome
    self._ativo = False
    Biblioteca.bibliotecas.append(self)

  def __str__(self):
    return self.nome

  @classmethod
  def listar_bibliotecas(cls):
    print(f"{'Nome da biblioteca'.ljust(25)} | {'Status'}")
    for biblioteca in cls.bibliotecas:
      print(f'{biblioteca.nome.ljust(25)} | {biblioteca.ativo}')

  #Método set no Python
  def alterna_estado(self):
    self._ativo = not self._ativo

  #Método get no Python
  @property
  def ativo(self):
    return "ativada" if self._ativo else "desativada"
  
  def receber_avaliacao(self, cliente, nota):
    avaliacao = Avaliacao(cliente, nota)
    self._avaliacao.append(avaliacao)

  @property # Atraves da property, podemos utilizar um metodo ou variavel sem estar no atributo na classe
  def media_avaliacoes(self):
    if not self._avaliacoes:
      return "-"
    soma = sum(avaliacao.nota for avaliacao in self._avaliacao)
    media = round(soma/len(self._avaliacao), 1)
    return media
  
  def adicionar_item(self, item):
    if isinstance(item, ItemBiblioteca):
      self._itens.append(item)


  def exibir_itens(self):
    print(f'Itens da Biblioteca {self.nome}\n')
    for i, item in enumerate(self._itens, start=1):
      if hasattr(item, "isbn"):
        msg_livro = f"{i}. Título: {item._titulo} | Autor: {item._autor} | Preço: {item._preco} | ISBN: {item.isbn}"
        print(msg_livro)
      else:
        msg_revista = f"{i}. Título: {item._titulo} | Autor: {item._autor} | Preço: {item._preco} | Edição: {item.edicao}"
        print(msg_revista)

  

    

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shoppping")

print(biblioteca_cidade)
biblioteca_cidade.alterna_estado()
print(biblioteca_shopping)

Biblioteca.listar_bibliotecas()
