# Task 1.
# Create a class that descibes a Product of online store. As a Product fields you can use a price, description and product' dimensions.
# Create a class that describes a Customer. As a Customer fields you can use surname, name, patronymic, mobile phone, etc.
# Create a class that describes an Order.
# - the order must contain data about the customer who carried it out and products. Implement a method for calculating the total order value.

class Product:
	def __init__(self, price, description, dimentions):
		self.price = price
		self.description = description
		self.dimentions = dimentions


	def __str__(self):
		return f"\nProduct: Description - {self.__description}, Price - {self.__price}, Dimentions - {self.__dimentions}"


	@property 
	def price(self):
		return self.__price


	@price.setter
	def price(self, value):
		if not isinstance(value, int):
			raise TypeError("Wrong value type")
		self.__price = value


	@property 
	def description(self):
		return self.__description


	@description.setter
	def description(self, value):
		if not isinstance(value, str):
			raise TypeError("Wrong value type")
		self.__description = value


	@property 
	def dimentions(self):
		return self.__dimentions


	@dimentions.setter
	def dimentions(self, value):
		if not isinstance(value, str):
			raise TypeError("Wrong value type")
		self.__dimentions = value


class Customer:
	def __init__(self, new_surname: str, new_name: str, 
				new_patronymic: str, new_number: str):
		self.surname = new_surname
		self.name = new_name
		self.patronymic = new_patronymic
		self.phone_number = new_number

	def __str__(self):
		return f"Customer:\nName - {self.__name}\nSurname - {self.__surname}\
			\nPatronymic - {self.__patronymic}\nPhone number - {self.__phone_number}"

		
	@property
	def name(self):
		return self.__name


	@name.setter
	def name(self, value):
		if not isinstance(value, str):
			raise TypeError("Wrong value type")
		self.__name = value


	@property
	def surname(self):
		return self.__surname


	@surname.setter
	def surname(self, value):
		if not isinstance(value, str):
			raise TypeError("Wrong value type")
		self.__surname = value


	@property
	def patronymic(self):
		return self.__patronymic


	@patronymic.setter
	def patronymic(self, value):
		if not isinstance(value, str):
			raise TypeError("Wrong value type")
		self.__patronymic = value


	@property
	def phone_number(self):
		return self.__phone_number


	@phone_number.setter
	def phone_number(self, value):
		if not isinstance(value, str):
			raise TypeError("Wrong value type")
		self.__phone_number = value



class Order:

	def __init__(self, customer: Customer,  *args:Product):
		self.customer = customer
		self.products_ordered = args

	@property
	def customer(self):
		return self.__customer


	@customer.setter
	def customer(self, value):
		if not isinstance(customer, Customer):
			raise TypeError("Wrong value type")
		self.__customer = value

	@property
	def products_ordered(self):
		return self.__products_ordered

	@products_ordered.setter
	def products_ordered(self, value):
		if not all(isinstance(prod, Product) for prod in value):
			raise TypeError("Wrong value type")
		self.__products_ordered = value


	def __str__(self):
		return f'{self.customer} \n {" ".join(map(str, self.products_ordered))}'
		

	def order_price(self) -> int:
		"""Returns the sum of prices of all ordered products"""
		return sum(i.price for i in self.products_ordered)


product1 = Product(111, "Stone", '300x300x300')
product2 = Product(1000, 'Wood', '300x300x300')
customer = Customer("Gromyako", "Vitaliy", "Yurevich", '88005553535')

print(customer)

order = Order(customer, product1, product2)
print(order)
print(f'Full price: {order.order_price()}')
