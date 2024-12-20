import streamlit as st
from time import sleep
from preprocessing.cleaning_data import Property, preprocess
from predict.prediction import predict

image_path = "./utils/house_header.jpg"

st.image(image_path, caption=None, use_container_width=True)

st.title("Immo Eliza Prediction App")
st.write("Welcome! Please enter the property details below.")
st.write('When finished, click on "Predict price".')

type_of_property = st.selectbox("Type of property:", ["House", "Apartment"])

subtype_of_property = st.selectbox(
    "Sub-type of property:",
    [
        "House",
        "Apartment",
        "Apartment block",
        "Bungalow",
        "Country cottage",
        "Duplex",
        "Exceptional property",
        "Farmhouse",
        "Flat studio",
        "Ground floor",
        "Kot",
        "Loft",
        "Mansion",
        "Penthouse",
        "Service flat",
        "Town house",
        "Triplex",
        "Villa",
    ],
)

living_area = st.text_input('Living area:", "In square meters...')

building_condition = st.selectbox(
    "Building condition:", ["To restore", "To renovate", "Good"]
)

equipped_kitchen = st.selectbox(
    "State of the kitchen", ["Not installed", "Installed", "Equipped"]
)

terrace = st.text_input(
    "Size of the terrace: If there is no terrace, please enter zero (0)."
)
garden = st.text_input(
    "Size of the garden: If there is no garden, please enter zero (0)."
)
facade_number = st.text_input("Number of facades: ")
zip_code = st.text_input("Zip code:")
province = st.selectbox(
    "Province",
    [
        "Antwerp",
        "Brussels",
        "East Flanders",
        "Flemish Brabant",
        "Hainaut",
        "Liege",
        "Limburg",
        "Luxembourg",
        "Namur",
        "Walloon Brabant",
        "West Flanders",
    ],
)


def prop_compatibility():
    """
    Returs true if the selected type and subtype of property correspond to the same cathegory.
    Eg. A kot cannot belong to the category "House"
    Otherwise, it returns false.
    """

    houses = [
        "House",
        "Bungalow",
        "Country cottage",
        "Duplex",
        "Exceptional property",
        "Farmhouse",
        "Loft",
        "Mansion",
        "Town house",
        "Triplex",
        "Villa",
    ]
    apartments = [
        "Apartment",
        "Apartment block",
        "Flat studio",
        "Ground floor",
        "Kot",
        "Penthouse",
        "Service flat",
    ]
    if (
        type_of_property == "House"
        and subtype_of_property in apartments
        or type_of_property == "Apartment"
        and subtype_of_property in houses
    ):
        st.error(
            f"Please correct property type and sub-type. \n {subtype_of_property} does not belong to the category {type_of_property}"
        )
        return False
    else:
        return True


if st.button("Predict price"):

    if prop_compatibility():

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

            loading_img = "./utils/loading.gif"
            placeholder = st.image(loading_img, caption=None, width=60)

            house = Property(
                type_of_property,
                subtype_of_property,
                living_area,
                building_condition,
                equipped_kitchen,
                terrace,
                garden,
                facade_number,
                zip_code,
                province,
            )

            processed_data = preprocess(house)
            prediction = predict(processed_data)
            sleep(0.5)
            placeholder.empty()
            st.write(f"The predicted price for this property is: {prediction}")
