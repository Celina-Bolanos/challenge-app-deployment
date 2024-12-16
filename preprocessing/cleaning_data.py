from math import radians, sin, cos, sqrt, atan2
import pandas as pd

# Convert functions with the zip code to class:
class ZipCode():
    """
    Integer number corrsponding to a location zip code.
    """
    def __init__(self, zip_code):
        self.zip_code = zip_code
        self.latitude = None
        self.longitude = None
        self.get_coordinates()
    
    def __str__(self):
        return f'Zipcode: {self.zip_code}'
    
    def get_coordinates(self):
        zip_codes_df = pd.read_csv('utils/zipcode_belgium.csv')
        row = zip_codes_df[zip_codes_df["zip_code_col"] == self.zip_code]
        self.latitude = float(row["latitude"].values[0])
        self.longitude = float(row["longitude"].values[0])


# Convert functions with the province to class:
class Province():
    """
    A belgian province and its capital coordinates
    """
    def __init__(self, name):
        self.name = name
        self.latitude = None
        self.longitude = None
        self.get_coordinates()
    
    def __str___(self, name):
        return f'This is the belgian provice of {name}.'

    
    def get_coordinates(self):
        """
        Returns the laitude and longitude of the province's capital.
        """
        provinces_df = pd.read_csv('utils/provinces_zip_codes.csv')
        province_data = provinces_df[provinces_df["province"] == self.name]
        self.latitude = float(province_data["latitude"].values[0])
        self.longitude = float(province_data["longitude"].values[0])
    
    def get_distance(self, lat1, lon1):
        """
        Returs the distance between the provice's capital and
        a property's zip code.

        PARAMS:
        lat1 -float: latitude to calculate the distance from
        lon1 -float: longitude to calculate the distance from

        RETURN
        Distance in kilometers, rounded to two decimal points
        """
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, self.latitude, self.longitude])

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        # Earth's radius in kilometers
        radius_of_earth_km = 6371

        # Calculate distance
        distance = round(radius_of_earth_km * c, 2)
        return distance


# Create a property class to instantiate an object on API:
class Property():
    """
    Defines a real state property.
    """
    sub_types_dict = {
        "kot": 0, "flat studio": 1, "service flat": 2,
        "bungalow": 3, "town house": 4, "ground floor": 5, "apartment": 6,
        "house": 7, "triplex": 8, "farmhouse": 9, "loft": 10, "duplex": 11,
        "apartment block": 12, "country cottage": 13, "penthouse": 14,
        "mansion": 15, "villa": 16, "exceptional property": 17,
        }
    
    building_statuses = {'To restore': 0, 'To renovate': 1, 'Good': 2}
    kitchen_statuses = {'Not installed': 0, 'Installed': 1, 'Equipped': 2}

    def __init__(self, type_of_property, subtype_of_property, living_area,
                 building_condition, equipped_kitchen, terrace, garden,
                 facade_number, zip_code, province):

        self.type_of_property = type_of_property
        self.subtype_of_property = subtype_of_property
        self.living_area = living_area
        self.building_condition = building_condition
        self.equipped_kitchen = equipped_kitchen
        self.terrace = terrace
        self.garden = garden
        self.facade_number = facade_number
        self.zip_code = zip_code
        self.province = province
        self.latitude = None
        self.longitude = None
        self.distance_to_capital = None
    
    def __str__(self):
        return f'A property located in {self.province}.'

    def encode_type_of_property(self):
        """Converts type of property to ordinal number."""
        self.type_of_property =  0 if self.type_of_property == 'Apartment' else 1
        return self.type_of_property

    def encode_subtype_of_property(self):
        """Converts sub-type of property to ordinal number."""
        self.subtype_of_property = self.sub_types_dict.get(self.subtype_of_property)
        return self.subtype_of_property

    def encode_building_condition(self):
        """Converts property condition of property to ordinal number."""
        self.building_condition = self.building_statuses.get(self.building_condition)
        return self.building_condition

    def encode_kitchen_status(self):
        """Converts kitchen's state of the property to ordinal number."""
        self.equipped_kitchen = self.kitchen_statuses.get(self.equipped_kitchen)
        return self.equipped_kitchen

    def calc_coordinates(self):
        """Calculates the distance of the property to the provice's capital."""
        zip_code_obj = ZipCode(self.zip_code)
        self.latitude = zip_code_obj.latitude
        self.longitude = zip_code_obj.longitude

        province_obj = Province(self.province)
        self.distance_to_capital = province_obj.get_distance(self.latitude, self.longitude)

    def to_dataframe(self):
        """Converts the property object to a dataframe"""
        property_data = {
            'type_of_property': self.type_of_property,
            'subtype_of_property': self.subtype_of_property,
            'living_area': self.living_area,
            'building_condition': self.building_condition,
            'equipped_kitchen': self.equipped_kitchen,
            'terrace': self.terrace,
            'garden': self.garden,
            'facade_number': self.facade_number,
            'zip_code': self.zip_code,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'distance_to_capital': self.distance_to_capital,
        }
        print('House df:')
        print(pd.DataFrame([property_data]))
        return pd.DataFrame([property_data])


# Function that will call the property methods and convert it
def preprocess(property):
    """
    Returns a numpy array of the property details for prediction.

    PARAMS:
    property -object: that contains the property details and methods

    RETURNS
    property -pandas data frame: with the encoded property's info.
    """

    property.living_area = int(property.living_area)
    property.terrace = int(property.terrace)
    property.garden = int(property.garden)
    property.facade_number = int(property.facade_number)
    property.zip_code = int(property.zip_code)

    property.encode_type_of_property()
    property.encode_subtype_of_property()
    property.encode_building_condition()
    property.encode_kitchen_status()
    property.calc_coordinates()
    property_df = property.to_dataframe()
    property = property_df.values
    print('House nd array:')
    print(property)
    return property
