# Task 1.
# Create a class that descibes a Product of online store. As a Product fields you can use a price, description and product' dimensions.
# Create a class that describes a Customer. As a Customer fields you can use surname, name, patronymic, mobile phone, etc.
# Create a class that describes an Order.
# - the order must contain data about the customer who carried it out and products. Implement a method for calculating the total order value.
from dataclasses import dataclass

@dataclass
class Product:

    price:int
    description:str
    dimentions:str


    def __init__(self, new_price: int, new_description: str, new_dimentions: str):
        if not (isinstance(new_price, int) and  isinstance(new_description, str) and isinstance(new_dimentions, str)):

            raise TypeError("Wrong value type")
        self.price = new_price
        self.description = new_description
        self.dimentions = new_dimentions


@dataclass
class Customer:
    surname: str
    name: str
    patronymic: str
    phone_number: str

    def __init__(self, new_surname: str, new_name: str, 
                new_patronymic: str, new_number: str):

        if not (isinstance(new_surname, str) and  isinstance(new_name, str) and isinstance(new_patronymic, str) 
                and isinstance(new_number, str)):
            raise TypeError("Wrong value type")

        self.surname = new_surname
        self.name = new_name
        self.patronymic = new_patronymic
        self.phone_number = new_number


class Order:

    def __init__(self, customer: Customer,  *args:Product):
        self.customer = customer
        self.products_ordered = args


    def __str__(self):
        return f'{self.customer}: \n {self.products_ordered}'
    

    def count(self) -> int:
        full_price = 0
        for i in self.products_ordered:
            full_price += i.price
        return full_price

product1 = Product(500,' Stone', '300x300x300')
product2 = Product(1000, 'Wood', '300x300x300')
slava = Customer("Moskalenko", "Slava", "Alexandrovich", '88005553535')

order = Order(slava, product1, product2)
print(order)
print(order.count())
