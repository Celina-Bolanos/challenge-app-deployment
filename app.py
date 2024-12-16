import streamlit as st

from preprocessing.cleaning_data import Property, preprocess
from predict.prediction import predict

st.title('Immo Eliza Prediction App')
st.write('Welcome! Please enter the property details below.')
st.write('When finished, click on "Predict price".')

type_of_property = st.selectbox(
        'Type of property:',
        ['House', 'Apartment']
    )

subtype_of_property = st.selectbox(
        'Sub-type of property:',
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

living_area = st.text_input('Living area:", "In square meters...')

building_condition = st.selectbox(
        'Building condition:',
        ['To restore', 'To renovate', 'Good']
    )

equipped_kitchen = st.selectbox(
        'State of the kitchen',
        ['Not installed', 'Installed', 'Equipped']
    )

terrace = st.text_input('Size of the terrace: If there is no terrace, please enter zero (0).')
garden = st.text_input('Size of the garden: If there is no garden, please enter zero (0).')
facade_number = st.text_input('Number of facades: ')
zip_code = st.text_input('Zip code:')
province = st.selectbox(
        'Province',
       ['Antwerp',
 'Brussels',
 'East Flanders',
 'Flemish Brabant',
 'Hainaut',
 'Liege',
 'Limburg',
 'Luxembourg',
 'Namur',
 'Walloon Brabant',
 'West Flanders']
    )

if st.button('Predict'):
    
    if not living_area.isdigit():
        st.error("Please enter a valid number for the living area.")
    
    elif not terrace.isdigit():
        st.error("Please enter a valid number for the terrace area.")
    
    elif not garden.isdigit():
        st.error("Please enter a valid number for the garden area.")

    elif not facade_number.isdigit():
        st.error("Please enter a valid number for the number of facades.")
    
    elif not zip_code.isdigit() or len(zip_code) > 4:
        st.error("Please enter a valid number for the zip code.")
    
    else:

        house = Property(type_of_property, subtype_of_property, living_area, building_condition,
                        equipped_kitchen, terrace, garden, facade_number, zip_code, province)
        
        processed_data = preprocess(house)
        
        prediction = predict(processed_data)
        st.write(f'The predicted price for this property is: {prediction}')
