from src.item import Item

#class to represent a customer order
class Order:
	def __init__(self):
		self._id = -1
		self._status = "ordering"
		self._items = []	#list of strings + MainOrderItem
		self._net_price = 0
		
	#function to add items to the order. item is type String or MainOrderItem
	def add_item(self, item, price):
		self._items.append(item)
		self._net_price += price
		return
		
	#function to remove items from the order. item is type String or MainOrderItem 
	def remove_item(self, item, price):
		if not item in self._items:
			return False
		self._items.remove(item)
		self._net_price -= price		
		return True

	# function that removes all items in order
	@property
	def remove_all_items(self):
		self._items.clear()
		self._net_price = 0
		return
		
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
		output = ''
		output += f'Order ID: {self._id}\n'
		output += f'Status: {self._status}\n'
		output += f'Items: {self._items}\n'
		output += f'Price: ${self._net_price:.2f}'
		return output		 

	__repr__ = __str__
	
