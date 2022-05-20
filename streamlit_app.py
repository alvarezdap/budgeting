import streamlit as st

st.title('Budgeting tool')

ingreso = st.number_input('Earnings', 0, 10000)
egreso = st.number_input('Spendings',0,10000)
ahorro = st.number_input('Savings',0,100000)
tiempo_fondo_emergencia = st.radio('Months for Emergency Fund Calculation', [3, 6, 10, 12])
balance = ingreso - egreso
fondo_emergencia = egreso*tiempo_fondo_emergencia
inversion = ahorro - fondo_emergencia

st.title("Emergency fund")
st.markdown(fondo_emergencia)

st.title('Savings potential')
st.markdown("This is the amount that you can increase your savings monthly:")
st.markdown(balance)

st.title("Investment")
st.markdown("This is the amount that you have for investing:")
st.markdown(inversion)
