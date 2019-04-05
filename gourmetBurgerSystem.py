from menu import Menu
from order import Order

#class to represent the system
class GourmetBurgerSystem:
	def __init__(self):
		self._current_orders = []
		self._current_orders_id = []
		self._ready_orders = []
		self._ready_orders_id = []
		self._last_order_id = 0
		self._menu_inventory = Menu()
	
	#class to place order and decrement inventory
	def new_order(self, order):
		order.set_id(self._last_order_id + 1)
		self._last_order_id += 1
		order.set_status("preparing") 
		self._current_orders.insert(0, order)
		self._current_orders_id.insert(order.get_id())
		self._menu_inventory.dec_inventory(order.get_items())	
		
	def update_current_order(self, order_id):
		if(self._current_orders_id.count(order_id) == 1):
			index = self._current_orders_id.index(order_id)
			order = self._current_orders.pop([index])
			order.set_status("pickup")	
			self._ready_orders.append(order)
			self._ready_orders_id.append(self._current_orders_id.pop([index])
		else:
			print("order does not exist") 
			
	def update_ready_order(self, order_id):
		pass
		
		
	def check_order_status(self, order_id):
		if(self._current_orders_id.count(order_id) == 1):
			index = self._current_orders_id.index(order_id)
			return self._current_orders[index].get_status
		elif(self._ready_orders_id.count(order_id) == 1):
			index = self._ready_orders_id.index(order_id)
			return self._ready_orders[index].get_status
		else:
			print("order not current nor ready")
		
	def refill_inventory():
		pass
		
	def login():
		pass
