import menuItemSubClasses

class Order:
	def __init__(self, id, status):
		self._id = id
		self._status = status
		self._items = []
		self._net_price = float(-1)
		
	def add_item(self, item):
		self._items.insert(item)
	
	def remove_item(self, item):
		pass
		
	def calc_price(self):
		total = 0.00
		for x in self._items:
			total = total + x.get_price()
		return total
		
	def get_id(self):
		return self._id
		
	def set_id(self, id):
		self._id = id
		
	def get_status(self):
		return self._status
		
	
