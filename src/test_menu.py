from menu import *

class TestMenu():
	def setup_method(self):
		self.menu = Menu()

	def test_set_quantity(self):
        #pass an object of class BaseItem
		self.menu.add_base_item("nugget", 0, 1000, "side", ["small nuggets", "medium nuggets", "large nuggets"])
		self.menu.add_measured_item("small nuggets", 3.0, -1, "side", 3, "nuggets") 
		self.menu.add_measured_item("medium nuggets", 5.0, -1, "side", 6, "nuggets")
		self.menu.add_measured_item("large nuggets", 7.0, -1, "side", 10, "nuggets") 
		self.menu.set_quantity("nugget")
		assert(self.menu.get_item("small nuggets").stock_quantity == 1000/3)
		assert(self.menu.get_item("medium nuggets").stock_quantity == 1000/6)        
		assert(self.menu.get_item("large nuggets").stock_quantity == 1000/10)    
        
        #pass an object not of class BaseItem
		assert(self.menu.set_quantity("small nuggets") == False)  

        #item not on menu
		assert(self.menu.set_quantity("fillet o fish") == False)   

        #stock_quantity of base item is 0
		nugget = self.menu.get_item("nugget")
		nugget.stock_quantity = 0
		self.menu.set_quantity("nugget")          
		assert(self.menu.get_item("small nuggets").stock_quantity == 0)
		assert(self.menu.get_item("medium nuggets").stock_quantity == 0)        
		assert(self.menu.get_item("large nuggets").stock_quantity == 0)

        #stock_quantity of base item is < serving_size
		nugget = self.menu.get_item("nugget")
		nugget.stock_quantity = 2
		self.menu.set_quantity("nugget")          
		assert(self.menu.get_item("small nuggets").stock_quantity == 0)
		assert(self.menu.get_item("medium nuggets").stock_quantity == 0)        
		assert(self.menu.get_item("large nuggets").stock_quantity == 0)
		
	def test_check_enough_inventory1(self):
		#main item enough inventory
		self.menu.add_menu_item("sesame bun", 1, 1000, "ingredient")
		self.menu.add_menu_item("beef patty", 1.5, 1000, "ingredient") 
		self.menu.add_menu_item("tomato", 0.5, 1000, "ingredient") 
		burger = MainOrderItem("single burger", 4, ["sesame bun", "sesame bun", "beef patty", "tomato"])
		insufficient = self.menu.check_enough_inventory([burger])
		assert(len(insufficient) == 0)
		
	def test_check_enough_inventory2(self):
		#main item not enough inventory
		self.menu.add_menu_item("sesame bun", 1, 1, "ingredient")
		self.menu.add_menu_item("beef patty", 1.5, 0, "ingredient") 
		self.menu.add_menu_item("tomato", 0.5, 0, "ingredient") 
		burger = MainOrderItem("single burger", 4, ["sesame bun", "sesame bun", "beef patty", "tomato"])
		insufficient = self.menu.check_enough_inventory([burger])
		assert(len(insufficient) == 3)
		assert(insufficient["sesame bun"] == 1)
		assert(insufficient["beef patty"] == 0)		
		assert(insufficient["tomato"] == 0)        


