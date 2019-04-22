from src.gourmetBurgerSystem import *
from src.menu_creator import *
import pytest

class TestCurrentOrders():
	def setup_method(self):
		self.system = GourmetBurgerSystem(create_menu())
      

	# testing order refill functions
	def test_refill_inventory(self):
		menu = self.system.dsiplay_inventory
		

	# test for seeing the inventory
	def test_view_inventory(self):
