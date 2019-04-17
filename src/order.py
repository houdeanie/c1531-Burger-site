from menuItem import MenuItem

#class to represent a customer order
class Order:
	def __init__(self):
		self._id = -1
		self._status = "ordering"
		self._items = []
		self._net_price = 0
		
	#classes to items in the order
	def add_item(self, item, price):
		self._items.append(item)
		self._net_price += price
		return
	
	def remove_item(self, item, price):
		if not item in self._items:
			return False
		index = self._items.index(item)
		self._items.pop(index)
		self._net_price -= price
		return True
		
	#getter and setter methods	
	@property
	def id(self):
		return self._id
	
	@id.setter	
	def id(self, value):
		self._id = value
	
	@property	
	def status(self):
		return self._status
		
	@status.setter	
	def status(self, status):
		self._status = status
	
	@property	
	def items(self):
		return self._items
	
	@property	
	def net_price(self):
		return self._net_price	
	
	#modified print output
	def __str__(self):
		return str("id: {0}, status: {1}, items: {2}, net_price: ${3}".format(self._id, self._status, self._items, self._net_price))		 

		
	
