class Menu:
	def __init__(self, mains, bun_types, patty_types, wrap_types, filling_types, ingredients, sides, drinks, unavailable):
		self._mains = mains
		self._bun_types = bun_types
		self._patty_types = patty_types
		self._wrap_types = wrap_types
		self._filling_types = filling_types
		self._ingredients = ingredients
		self._sides = sides
		self._drinks = drinks
		self._unavailable = unavailable
		
	def update_unavailable(self):
		pass
		
	def dec_inventory(self, order):
		pass
		
	def add_unavailable(self, item):
		self._unavailable.insert(0, item)
		
	def remove_unavailable(self, item):
		pass
