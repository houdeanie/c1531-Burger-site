from menuItem import Ingredient

#class to represent a customer order
class Order:
	def __init__(self):
		self._id = -1
		self._status = "ordering"
		self._items = []
		self._net_price = float(-1)
		
	#classes to items in the order
	def add_item(self, item):
		self._items.insert(item)
	
	def remove_item(self, item):
		pass
	
	#class to calculate total price of order
	def calc_price(self):
		total = 0.00
		for x in self._items:
			total = total + x.get_price()
		return total
		
	#getter and setter methods	
	def get_id(self):
		return self._id
		
	def set_id(self, id):
		self._id = id
		
	def get_status(self):
		return self._status
		
	def set_status(self, status):
		self._status = status
	
	#function to print items in the order
	def show_items(self):
		if(len(self._items) == 0):
			return "none"
		else:
			items = []
			for x in self._items:
				items.append(x.get_name())
		return items
	
	#modified print output
	def __str__(self):
		print("id: {0}, status: {1}, items: {2}, net_price: {3}".format(self._id, self._status, self.show_items(), self._net_price))		 

		
	
