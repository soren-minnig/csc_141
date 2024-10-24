# Creating the function
def make_car(manufacturer, model, **information):
    information['manufacturer'] = manufacturer
    information['model'] = model
    return information

# Calling and printing the function
car = make_car('subaru', '2024 BRZ', color='white', horsepower='228')
print(car)