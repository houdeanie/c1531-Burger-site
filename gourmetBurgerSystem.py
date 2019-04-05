from menu import Menu
from order import Order

class GourmetBurgerSystem:
	def __init__(self):
		self._current_orders = []
		self._ready_orders = []
		self._last_order_id = 0
		self._menu_inventory = Menu()
			
	def new_order(self, order):
		order.set_id(self._last_order_id + 1)
		order.set_status("preparing") 
		self._current_orders.insert(0, order)
		#decrementInventory
		#update unavailable menu items
		
	#def update_order(self, order, status = "ready for pickup"):
	#	i = 0
	#	while(self._items[i].get_id() != order.get_id):
	#		i=+
		 	
		
		
	#def remove_order(self, 
	
