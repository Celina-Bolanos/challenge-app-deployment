import streamlit as st

from preprocessing.cleaning_data import Property
#from predict.prediction import predict

#house = Property()

st.title('Immo Eliza Prediction App')
st.write('Welcome! Please enter the property details below.')
st.write('When finished, click on "Predict price".')

type_of_property = st.selectbox(
        'Type of property:',
        ['House', 'Apartment']
    )

subtype_of_property = st.selectbox(
        'Type of property:',
        ['House','Apartment',
        'Apartment block',
        'Bungalow',
        'Castle',
        'Chalet',
        'Country cottage',
        'Duplex',
        'Exceptional property',
        'Farmhouse',
        'Flat studio',
        'Ground floor',
        'Kot',
        'Loft',
        'Manor house',
        'Mansion',
        'Penthouse',
        'Service flat',
        'Town house',
        'Triplex',
        'Villa']
    )




#house = Property()