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

if opcao == 'GTR':
    diaria = 440

elif opcao == 'BMW':
    diaria = 250

elif opcao == 'Porsche':
    diaria = 380

elif opcao == 'Ferrari':
    diaria = 700

elif opcao == 'Maserati':
    diaria = 500




if st.button('Caucular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')

