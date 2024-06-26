from utils.import_functions import import_car_plate, import_car_brand

# get the license plate
selected_plate = input("Insert the license plate: \n")

# use the plate for the function
cars_list = import_car_plate(selected_plate)

print(cars_list)