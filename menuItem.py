class MenuItem:
	def __init__(self, name, price, quantity, type):
		self._name = name
		self._price = price
		self._quantity = quantity
		self._type = type

	def get_name(self):
		return self._name
		
	def set_name(self, name):
		self._name = name
		
	def get_price(self):
		return self._price
	
	def set_price(self, price):
		self._price = price
		
	def get_quantity(self):
		return self._quantity
		
	def set_quantity(self, quantity):
		self._quantity = quantity
		
	def get_type(self):
		return self._type
		
	def set_type(self, type):
		self._type = type
		
class Main(MenuItem):
	def __init__(self, name, price, quantity, type):
		super().__init__(name, price, quantity, type)
		self._ingredients = []
		
	def calc_price(self):
		total = 0.00
		for x in self._ingredients:
			total = total + x.get_price()
		return total
		
	def get_ingredients(self):
		return self._ingredients
		
	def add_ingredient(self, ingredient):
		self._ingredients.insert(0, ingredient)
		
class Ingredient(MenuItem):
	def __init__(self, name, price, quantity, type):
		super().__init__(name, price, quantity, type)
		
class MeasuredItem(MenuItem):
	def __init__(self, name, price, quantity, type, serving_size):
		super().__init__(name, price, quantity, type)
		self._serving_size = serving_size
		
	def get_serving_size(self):
		return self._serving_size
		
	def set_serving_size(self, size):
		self._serving_size = size
	
	
	
		
