#! now, we dont want to hard code the attributes(instance attribute): __init__

class Item:
    def __init__(self, name: str, price: float, quantity=0):
        #Run validations to the received arguments
        assert price >=0, f"Price {price} is not grater than or equal to zero!"
        assert quantity >=0, f"Price {quantity} is not grater than or equal to zero!"

        #Assign to self object
        print(f"An instance created, Name: {name}, Price: {price}, Qt: {quantity}")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculateTotalPrice(self):#? we dont need to pass arguments here, cause they are already attributes in this class level
        return (self.price * self.quantity)


item1 = Item("Phone", 101, 6)
print(item1.calculateTotalPrice())



item2 = Item("Laptop", 1001, 4)
# Python will automatically print the 

#?adding more attributes to the instances
item2.hasNumpad = False 
