import requests


def import_car_plate(plate):
    '''
    Function to import RDW data based on the license plate

    Input:
    * plate: number plate of the car

    Output:
    * data: list with car data
    
    x522fd
    '''


    # define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={plate.upper()}"

    # execute the request
    response = requests.get(endpoint)

    # get the data from the response
    data = response.json()


    return data


def import_car_brand(brand):

    # define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand.upper()}"
    pass