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
