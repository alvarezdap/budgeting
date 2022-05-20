import streamlit as st

st.title('Budgeting tool')

st.slider('Earnings', 0, 10000)
st.slider('Spendings',0,10000)

st.slider('Savings',0,100000)
