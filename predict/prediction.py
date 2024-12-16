from keras.saving import load_model
import pandas as pd
import numpy as np

filepath = 'model/model.keras' # To work locally, it must be '../model/model.keras'
model = load_model(filepath, custom_objects=None, compile=True, safe_mode=True)

house = {
        'type_of_property': 0, 
        'subtype_of_property': 2,
        'living_area': 85, 
        'building_condition': 2, 
        'equipped_kitchen': 1,
        'terrace': 3,
        'garden': 0,
        'facade_number': 3,
        'zip_code': 2180,
        'latitude': 51.2771,
        'longitude': 4.4176,
        'distance': 7.25  
    }

house_df = pd.DataFrame([house])

house = house_df.values

def predict(property):
    """Returns the predicted price of a property.
    PARAMS:
    propery nd.array: the encoded values of the property

    RETURNS
    price -float: the predicted price
    """
    prediction = model.predict(property)

    pred_price_l = prediction[0,0]
    

    return pred_price_l


predict(house)


#print(f'Scaled prediction: {pred_price_l}')
#print(type(pred_price_l))
#prediction_actual = np.expm1(pred_price_l)
#print(f'Prectiction actual: {prediction_actual}')
#print(type(prediction_actual))