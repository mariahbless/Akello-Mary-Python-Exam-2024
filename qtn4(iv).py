#Question 4iv

# creating a class and its attributes
class Car:
    def __init__(self,brand,name,color):
        self.brand = brand
        self.color = color
        self.name = name

car= Car("New model 2024","Marcedes benz","Greay")
print('This car has the following composition, order for yours now')
print(f"Brand: {car.brand}")
print(f"Color: {car.color}")
print(f"name : {car.name }")



