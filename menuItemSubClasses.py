from menuItem import *

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
	
	
	
		
