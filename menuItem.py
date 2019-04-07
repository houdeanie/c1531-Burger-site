#parent class for all food and drink items
class MenuItem:
	def __init__(self, name, price, quantity, type):
		self._name = name
		self._price = price
		self._quantity = quantity
		self._type = type

	#getter and setter functions
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
		
#subclass to represent mains		
class Main(MenuItem):
	def __init__(self, name, price, quantity, type):
		super().__init__(name, price, quantity, type)
		self._ingredients = []
		
	#function to calculate the total price of a main	
	def calc_price(self):
		total = 0.00
		for x in self._ingredients:
			total = total + x.get_price() * x.get_quantity()
		self._price = total
		return 
		
	def get_ingredients(self):
		return self._ingredients
	
	#function to add ingredients 	
	def add_ingredient(self, ingredient):
		self._ingredients.insert(0, ingredient)
		self.calc_price()
		return
	
	#function to show ingredients
	def show_ingredients(self):
		if (len(self._ingredients) == 0):
			return "none"
		else:
			ingredients = []
			for x in self._ingredients:
				ingredients.append(x.get_quantity())
				ingredients.append(x.get_name())

		return ingredients
		
	#modified print output	
	def __str__(self):
		return "name: {0}, price: {1}, quantity: {2}, type: {3}, ingredients: {4}".format(self._name, self._price, self._quantity, self._type, self.show_ingredients())
		
		
#subclass to represent ingredients that can be added to mains		
class Ingredient(MenuItem):
	def __init__(self, name, price, quantity, type):
		super().__init__(name, price, quantity, type)
		
	#modified print output	
	def __str__(self):
		return "name: {0}, price: {1}, quantity: {2}, type: {3}".format(self._name, self._price, self._quantity, self._type)
		
#subclass of items that come in quantities more than 1 - e.g. drinks, nuggets 
class MeasuredItem(MenuItem):
	def __init__(self, name, price, quantity, type, serving_size):
		super().__init__(name, price, quantity, type)
		self._serving_size = serving_size
		
	#getter and setter functions
	def get_serving_size(self):
		return self._serving_size
		
	def set_serving_size(self, size):
		self._serving_size = size
		
	#modified print output	
	def __str__(self):
		return "name: {0}, price: {1}, quantity: {2}, type: {3}, serving_size: {4}".format(self._name, self._price, self._quantity, self._type, self._serving_size)
		
class Nugget(MeasuredItem):
	_total_nuggets = 10000
	def __init__(self, name, price, quantity, type, serving_size):
		super().__init__(name, price, quantity, type, serving_size)
		
	def get_total_nuggets(self):
		return self._total_nuggets
		
	def set_total_nuggets(self, total):
		self._total_nuggets = total
			
class Fries(MeasuredItem):
	_fries_grams = 10000
	def __init__(self, name, price, quantity, type, serving_size):
		super().__init__(name, price, quantity, type, serving_size)
		
	def get_total_fries(self):
		return self._total_fries
		
	def set_total_fries(self, total):
		self._total_fries = total
		
class OrangeJuice(MeasuredItem):
	_total_orange_juice = 10000
	def __init__(self, name, price, quantity, type, serving_size):
		super().__init__(name, price, quantity, type, serving_size)
		
	def get_total_orange_juice(self):
		return self._total_orange_juice
		
	def set_total_orange_juice(self, total):
		self._total_orange_juice = total

		
