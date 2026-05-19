import streamlit as st

st.title("Blackline Performance - Aluguel de carros")
st.sidebar.title("aqui tem opçoes de carros")

st.subheader('escolha seu modelo ')
st.sidebar.image('logo.png.png')
carros = ['GTR','BMW','Porsche','Ferrari','Maserati']

opcao = st.sidebar.selectbox('Escolha o carro para alugar', carros)


st.image(f'{opcao}.png')
st.markdown(f'## você alugou o modelo: {opcao}')
st.markdown('---')


dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'quantos km você rodou com o {opcao}?')