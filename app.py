import streamlit as st

st.title('Immo Eliza Prediction App')
st.write('Welcome! Please enter the property details below.')
st.write('When finished, click on "Predict price".')

type_of_property = st.text_input('Property type: ')