from keras.models import load_model
import numpy as np

filepath = 'model/model.keras' # To work locally, it must be '../model/model.keras'
model = load_model(filepath, custom_objects=None, compile=True, safe_mode=True)

def predict(property):
    """Returns the predicted price of a property.
    PARAMS:
    propery nd.array: the encoded values of the property

    RETURNS
    price -float: the predicted price
    """
    prediction = model.predict(property)

    prediction_scaled = prediction[0,0]
    prediction_actual = np.expm1(prediction_scaled)
    rounded_actual = round(prediction_actual)

    return rounded_actual