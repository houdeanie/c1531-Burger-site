from menu import *
from order import Order
from errors import *

#class to represent the system
class GourmetBurgerSystem:
	def __init__(self):
		self._current_orders = []
		self._current_orders_id = []
		self._ready_orders = []
		self._ready_orders_id = []
		self._last_order_id = 0
		self._menu_inventory = Menu()
	
	#function to place order and decrement inventory
	def new_order(self, order):
		insufficient = self._menu_inventory.check_enough_inventory(order.get_items())
		try:
			check_order_error(order)
		except OrderError as err:
			return err.errors
		if(len(insufficient) == 0):
			order.set_id(self._last_order_id + 1)
			self._last_order_id += 1
			order.set_status("preparing") 
			self._current_orders.insert(0, order)
			self._current_orders_id.insert(0, order.get_id())
			self._menu_inventory.dec_inventory(order.get_items())
			return self._last_order_id
		else:
			print("Not enough of these items to fulfill order:") 
			for item in insufficient:
				print("{0} {1}".format(item, insufficient[item]))
		return	
		
	#function to update order from preparing to ready for pickup
	def update_current_order(self, order_id):
		if(self._current_orders_id.count(order_id) == 1):
			index = self._current_orders_id.index(order_id)
			order = self._current_orders.pop()
			order.set_status("pickup")	
			self._ready_orders.append(order)
			self._ready_orders_id.append(self._current_orders_id.pop(index))
		else:
			print("order does not exist") 
		return
		
	#function to get order status	
	def check_order_status(self, order_id):
		if(self._current_orders_id.count(order_id) == 1):
			index = self._current_orders_id.index(order_id)
			return self._current_orders[index].get_status()
		elif(self._ready_orders_id.count(order_id) == 1):
			index = self._ready_orders_id.index(order_id)
			return self._ready_orders[index].get_status()
		else:
			return("Order is not being prepared. Please check order id and try again")
		return
		
	def get_current_orders(self):
		return self._current_orders	
		
	#function to update order from ready to picked up		
	def update_ready_order(self, order_id):
		if(self._ready_orders_id.count(order_id) == 1):
			index = self._ready_orders_id.index(order_id)
			order = self._ready_orders.pop(index)
			self._ready_orders_id.pop(index)	
		return
		
	def get_menu(self):
		return self._menu_inventory.show_menu()
		
	def show_inventory(self):
		return self._menu_inventory.show_inventory()

		
	def get_copy(self, name, quantity): 
		return self._menu_inventory.get_copy(name, quantity)
		

		
	def refill_inventory():
		pass
		
	def login():
		pass