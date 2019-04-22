from src.gourmetBurgerSystem import *
from src.menu_creator import *
import pytest

class TestCurrentOrders():
	def setup_method(self):
		self.system = GourmetBurgerSystem(create_menu())
      
	# test for seeing the inventory
	def test_view_inventory(self):
		ingredients = self.system.display_inventory.get_ingredients()
		sides = self.system.display_inventory.get_measured_item('side')
		drinks = self.system.display_inventory.get_measured_item('drink')
		desserts = self.system.display_inventory.get_measured_item('dessert')

		assert(len(ingredients) == 14)
		assert(len(sides) == 6)
		assert(len(drinks) == 4)
		assert(len(desserts) == 6)

	# testing order refill functions
	def test_refill_inventory(self):
		refill = 100
		# test with ingredient
		s_bun1 = self.system.display_item('sesame bun')
		s_bun2 = self.system.display_inventory.get_stock_quantity('sesame bun')
		assert (s_bun1.stock_quantity == s_bun2)

		self.system.display_inventory.set_stock_quantity('sesame bun', refill)
		s_bun3 = self.system.display_item('sesame bun')
		assert (s_bun3.stock_quantity == refill)
		s_bun4 = self.system.display_item('sesame bun')
		s_bun4.stock_quantity += 900
		s_bun5 = self.system.display_item('sesame bun')
		assert(s_bun5.stock_quantity == 1000)
		
		# test with sides
		side1 = self.system.display_item('small nuggets')
		side1_base_name = side1.base_item
		side2 = self.system.display_item(side1_base_name)
		assert (side2.stock_quantity == 1000)
		side2.stock_quantity += 100
		side3 = self.system.display_item(side1_base_name)
		assert (side3.stock_quantity == 1100)
		

		self.system.display_inventory.set_stock_quantity('sesame bun', refill)
		side3 = self.system.display_item('sesame bun')
		assert (s_bun3/stock_quantity == refill)

		# test with drinks
		drink1 = self.system.display_item('small orange juice')
		drink1_base_name = drink1.base_item
		drink2 = self.system.display_item(drink1_base_name)
		assert (drink2.stock_quantity == 1000)
		drink2.stock_quantity += 100
		drink3 = self.system.display_item(drink1_base_name)
		assert (drink3.stock_quantity == 1100)

		# test with desserts
		dessert1 = self.system.display_item('small chocolate sundae')
		dessert1_base_name = dessert1.base_item
		dessert2 = self.system.display_item(dessert1_base_name)
		assert (dessert2.stock_quantity == 10000)
		dessert2.stock_quantity += 100
		dessert3 = self.system.display_item(dessert1_base_name)
		assert (dessert3.stock_quantity == 10100)


		
		

	
