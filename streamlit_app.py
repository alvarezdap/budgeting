import streamlit as st

st.title('Budgeting tool')

ingreso = st.slider('Earnings', 0, 10000)
egreso = st.slider('Spendings',0,10000)
ahorro = st.slider('Savings',0,100000)
balance = ingreso - egreso
fondo_emergencia = egreso*6

st.title("Emergency fund")
st.markdown(fondo_emergencia)

if ahorro > fondo_emergencia:
    st.balloons()
