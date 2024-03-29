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
	
	#create new Main Order Item	
	def new_main_order_item(self, name):
		main = MainOrderItem(name, 0, [])
		return main	
	
	#function to place order and decrement inventory
	def place_order(self, order, items):
		try:
			# check_order_error(order)
			pass
		except OrderError as err:
			return err.errors
		insufficient = self._menu_inventory.check_enough_inventory(items)
		new_order = Order()
		for item in items:
			if isinstance(item, MainOrderItem) and item.name.endswith("burger"):
				self.check_burger(item)
			new_order.add_item(item, item.price)
		# print(new_order)
		if(len(insufficient) > 0):
			raise OrderException("we don't have enough inventory to fulfil this order")
		if(len(insufficient) == 0):
			new_order.id = self._last_order_id + 1
			self._last_order_id += 1
			new_order.status = "preparing"
			self._order_history.append(new_order)
			self._menu_inventory.dec_inventory(new_order.items)
		# print(self.get_order(new_order.id))
			return new_order
		return None
		
	#function to update order from preparing to ready for pickup
	def update_order_pickup(self, order_id):
		order = self.get_order(order_id)
		if order == None:
			raise OrderException("order does not exist. Please check order id and try again")
		else:
			order.status = "ready"	
		return
		
	#function to update order from ready to picked up		
	def update_order_completed(self, order_id):
		order = self.get_order(order_id)		
		if order == None:
			raise OrderException("order does not exist. Please check order id and try again")
		else: 
			index = self._order_history.index(order)
			order = self._order_history.pop(index)
		return		
		
	#function to get order status	
	def check_order_status(self, order_id):
		order = self.get_order(order_id)
		if order == None:
			raise OrderException("order does not exist. Please check order id and try again")
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
	
	# takes in and item and returns dict of insufficent quantities
	def check_item_sufficient(self, item):
		return self._menu_inventory.check_enough_inventory(item)

    # checks if burger is valid
	def check_burger(self, item):
		ingredients = item.ingredients
		buns = 0
		patties = 0
		for key, value in ingredients.items():
			if key.endswith("bun"):
				buns += value
			if key.endswith("patty"):
				patties += value
		if buns < 2:
			raise OrderException("burger must have at least two buns")
		if buns > 4:
			raise OrderException("burger can have maximum 4 buns")
		if patties > 3:
			raise OrderException("burger can have maximum 3 patties")
		return




		
