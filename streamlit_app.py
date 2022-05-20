import streamlit as st

st.title('Budgeting tool')

ingreso = st.slider('Earnings', 0, 10000)
egreso = st.slider('Spendings',0,10000)
ahorro = st.slider('Savings',0,100000)
balance = ingreso - egreso
fondo_emergencia = egreso*6
inversion = ahorro - fondo_emergencia

st.title("Emergency fund")
st.markdown(fondo_emergencia)

st.title('Savings potential')
st.markdown("This is the amount that you can increase your savings monthly:")
st.markdown(balance)

st.title("Investment")
st.markdown("This is the amount that you have for investing:")
st.markdown(inversion)
