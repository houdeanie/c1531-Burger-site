from src.gourmetBurgerSystem import *
from src.order import *
from src.menu import *
from src.menuItem import *

class TestUS1A(object):
	
	def setup_method(self):
		self.system = GourmetBurgerSystem()
		
	def test_order_burger(self):
		burger = self.system.get_copy("burger", 1)
		burger.add_ingredient(self.system.get_copy("sesame_bun", 2))
		burger.add_ingredient(self.system.get_copy("tomato", 1))		
		burger.add_ingredient(self.system.get_copy("swiss_cheese", 1))			
		burger.add_ingredient(self.system.get_copy("beef_patty", 1))	
		burger.add_ingredient(self.system.get_copy("lettuce", 1))					
		burger.add_ingredient(self.system.get_copy("ians_special_sauce", 1))	
		order = Order()
		order.add_item(burger)
		self.system.new_order(order)	
		assert(self.system.get_current_orders()[0] == order)	
		
	def test_not_enough_ingredient(self):
		burger = self.system.get_copy("burger", 1)
		burger.add_ingredient(self.system.get_copy("sesame_bun", 2))	
		burger.add_ingredient(self.system.get_copy("beef_patty", 1))	
		burger.add_ingredient(self.system.get_copy("lettuce", 10000))	
		order = Order()				
		order.add_item(burger)
		self.system.new_order(order)	
		assert(len(self.system.get_current_orders()) == 0)	
		
	def test_order_drink(self):	
		burger = self.system.get_copy("burger", 1)
		burger.add_ingredient(self.system.get_copy("sesame_bun", 2))
		burger.add_ingredient(self.system.get_copy("tomato", 1))		
		burger.add_ingredient(self.system.get_copy("swiss_cheese", 1))			
		burger.add_ingredient(self.system.get_copy("beef_patty", 1))	
		burger.add_ingredient(self.system.get_copy("lettuce", 1))					
		burger.add_ingredient(self.system.get_copy("ians_special_sauce", 1))	
		drink = self.system.get_copy("small_orange_juice", 1)	
		order = Order()
		order.add_item(burger)
		order.add_item(drink)
		self.system.new_order(order)	
		assert(self.system.get_current_orders()[0] == order)
		
	def test_not_enough_drink(self): 
		drink = self.system.get_copy("small_orange_juice", 10000)	
		order = Order()				
		order.add_item(drink)
		self.system.new_order(order)	
		assert(len(self.system.get_current_orders()) == 0)	
		
	def test_order_side(self):
		burger = self.system.get_copy("burger", 1)
		burger.add_ingredient(self.system.get_copy("sesame_bun", 2))
		burger.add_ingredient(self.system.get_copy("tomato", 1))		
		burger.add_ingredient(self.system.get_copy("swiss_cheese", 1))			
		burger.add_ingredient(self.system.get_copy("beef_patty", 1))	
		burger.add_ingredient(self.system.get_copy("lettuce", 1))					
		burger.add_ingredient(self.system.get_copy("ians_special_sauce", 1))	
		drink = self.system.get_copy("small_orange_juice", 1)	
		side = self.system.get_copy("small_nuggets", 1)
		order = Order()
		order.add_item(burger)
		order.add_item(drink)
		order.add_item(side)
		self.system.new_order(order)	
		assert(self.system.get_current_orders()[0] == order)
		
	def test_not_enough_side(self):
		side = self.system.get_copy("small_nuggets", 10000)	
		order = Order()				
		order.add_item(side)
		self.system.new_order(order)	
		assert(len(self.system.get_current_orders()) == 0)			
							
class TestUS2(object):
	
	def setup_method(self):
		self.system = GourmetBurgerSystem()
	
	def test_get_order_status(self):
		burger = self.system.get_copy("burger", 1)
		burger.add_ingredient(self.system.get_copy("sesame_bun", 2))
		burger.add_ingredient(self.system.get_copy("tomato", 1))		
		burger.add_ingredient(self.system.get_copy("swiss_cheese", 1))			
		burger.add_ingredient(self.system.get_copy("beef_patty", 1))	
		burger.add_ingredient(self.system.get_copy("lettuce", 1))					
		burger.add_ingredient(self.system.get_copy("ians_special_sauce", 1))	
		drink = self.system.get_copy("small_orange_juice", 1)	
		side = self.system.get_copy("small_nuggets", 1)
		order = Order()
		order.add_item(burger)
		order.add_item(drink)
		order.add_item(side)
		order_id = self.system.new_order(order)	
		assert(order_id == 1)
		assert(order.get_net_price() == 13.00)
		order_id = self.system.new_order(order)	
		assert(order_id == 2)		
		 
class TestUS3(object):

	def setup_method(self):
		self.system = GourmetBurgerSystem()
		
	def test_check_order_status(self):
		burger = self.system.get_copy("burger", 1)
		burger.add_ingredient(self.system.get_copy("sesame_bun", 2))
		burger.add_ingredient(self.system.get_copy("tomato", 1))		
		burger.add_ingredient(self.system.get_copy("swiss_cheese", 1))			
		burger.add_ingredient(self.system.get_copy("beef_patty", 1))	
		burger.add_ingredient(self.system.get_copy("lettuce", 1))					
		burger.add_ingredient(self.system.get_copy("ians_special_sauce", 1))	
		drink = self.system.get_copy("small_orange_juice", 1)	
		side = self.system.get_copy("small_nuggets", 1)
		order = Order()
		order.add_item(burger)
		order.add_item(drink)
		order.add_item(side)
		order_id = self.system.new_order(order)	
		assert(self.system.check_order_status(order_id) == "preparing")	
		self.system.update_current_order(order_id)
		assert(self.system.check_order_status(order_id) == "pickup")
		self.system.update_ready_order(order_id)
		assert(self.system.check_order_status(order_id) == "Order is not being prepared. Please check order id and try again")
	
class TestUS4(object):

	def setup_method(self):
		self.system = GourmetBurgerSystem()	
	

	def test_update_order_status(self): 
		burger = self.system.get_copy("burger", 1)
		burger.add_ingredient(self.system.get_copy("sesame_bun", 2))
		burger.add_ingredient(self.system.get_copy("tomato", 1))		
		burger.add_ingredient(self.system.get_copy("swiss_cheese", 1))			
		burger.add_ingredient(self.system.get_copy("beef_patty", 1))	
		burger.add_ingredient(self.system.get_copy("lettuce", 1))					
		burger.add_ingredient(self.system.get_copy("ians_special_sauce", 1))	
		drink = self.system.get_copy("small_orange_juice", 1)	
		side = self.system.get_copy("small_nuggets", 1)
		order = Order()
		order.add_item(burger)
		order.add_item(drink)
		order.add_item(side)
		order_id = self.system.new_order(order)	
		assert(self.system.check_order_status(order_id) == "preparing")	
		self.system.update_current_order(order_id)
		assert(self.system.check_order_status(order_id) == "pickup")	
	
class TestUS5(object):

	def setup_method(self):
		self.system = GourmetBurgerSystem()	
		self.system1 = GourmetBurgerSystem()
		
	def test_dec_inventory(self): 	
		burger = self.system.get_copy("burger", 1)
		burger.add_ingredient(self.system.get_copy("sesame_bun", 2))
		burger.add_ingredient(self.system.get_copy("tomato", 1))		
		burger.add_ingredient(self.system.get_copy("swiss_cheese", 1))			
		burger.add_ingredient(self.system.get_copy("beef_patty", 1))	
		burger.add_ingredient(self.system.get_copy("lettuce", 1))					
		burger.add_ingredient(self.system.get_copy("ians_special_sauce", 1))	
		drink = self.system.get_copy("small_orange_juice", 1)	
		side = self.system.get_copy("small_nuggets", 1)
		order = Order()
		order.add_item(burger)
		order.add_item(drink)
		order.add_item(side)
		order_id = self.system.new_order(order)	
		assert(self.system.get_menu() == self.system1.get_menu())

