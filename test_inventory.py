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
		menu = self.system.dsiplay_inventory

		
		

	
