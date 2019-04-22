from src.gourmetBurgerSystem import *
from src.menu_creator import *
import pytest

class TestCurrentOrders():
	def setup_method(self):
		self.system = GourmetBurgerSystem(create_menu())
      

	# testing order refill functions
	def test_refill_inventory(self):
		

	# test for seeing the inventory
	def test_view_inventory(self):
