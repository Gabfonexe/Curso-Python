import streamlit as st
import dados

st.title("filme")
nome = st.text_input("Nome do Filme: ")
ano = st.number_input("Ano do Filme: ")
nota = st.slider("Nota do filme:", min_value=0.0, max_value=10.0)

if st.button('Adcionar'):
  dados.insere_dados(nome, ano, nota)
  st.success("Filme Cadastrado")

filmes =  dados.obter_dados()
st.header("lista de Filmes")
st.table(filmes)
