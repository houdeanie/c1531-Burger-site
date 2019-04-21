from src.menu import *
from src.order import Order
from src.errors import *

#class to represent the system
class GourmetBurgerSystem:
	def __init__(self, menu = None):
		self._order_history = []
		self._last_order_id = 0
		self._menu_inventory = menu or Menu()
	
	# use system to create new order
	def new_order(self):
		order = Order()
		return order	

	#create new Main Order Item	
	def new_main_order(self, name):
		main = MainOrderItem(name, 0, {})
		return main
	
	#function to place order and decrement inventory
	def place_order(self, items):
		#insufficient = self._menu_inventory.check_enough_inventory(order.items)
		#try:
		#	check_order_error(order)
		#except OrderError as err:
		#	return err.errors
		new_order = Order()
		for item in items:
			new_order.add_item(item, item.price)
		# print(new_order)
		#if(len(insufficient) == 0):
		new_order.id = self._last_order_id + 1
		self._last_order_id += 1
		new_order.status = "preparing"
		self._order_history.append(new_order)
		self._menu_inventory.dec_inventory(new_order.items)
		# print(self.get_order(new_order.id))
		return new_order
		#else:
		#	print("Not enough of these items to fulfill order:") 
		#	for item in insufficient:
		#		print("{0} {1}".format(item, insufficient[item]))
		#return None
		
	#function to update order from preparing to ready for pickup
	def update_order_pickup(self, order_id):
		order = self._get_order(order_id)
		if order == None:
			return None
		else:
			order.status = "ready"	
		return
		
	#function to update order from ready to picked up		
	def update_order_completed(self, order_id):
		order = self._get_order(order_id)		
		if order == None:
			return None		
		else: 
			index = self._order_history.index(order)
			order = self._order_history.pop(index)
		return		
		
	#function to get order status	
	def check_order_status(self, order_id):
		order = self._get_order(order_id)
		if order == None:
			return("Order is not being prepared. Please check order id and try again")
		else:
			return order.status
		return

	#function to get current orders	
	def get_current_orders(self):
		current_orders = [order for order in self._order_history if order.status == "preparing"]
		return current_orders
				
	#function to look for order_id in order history and returns the order			
	def get_order(self, order_id):
		for order in self._order_history:
			if int(order.id) == int(order_id):
				return order
		return None
	
	#get menu	
	def get_menu_items(self):
		return self._menu_inventory.get_items()
	
	# returns the menu class 	
	@property
	def display_inventory(self):
		return self._menu_inventory

	#display item	
	def display_item(self, name):
		if name == "":
			return "Item name is empty"
		if not self._menu_inventory.get_item(name):
			return "Item doesn't exist"
		return self._menu_inventory.get_item(name)
	
	def refill_inventory(self):
		self._menu_inventory.refill_inventory()
		
