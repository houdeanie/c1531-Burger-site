from src.gourmetBurgerSystem import *
from src.menu_creator import *
import pytest

class TestCurrentOrders():
	def setup_method(self):
		self.system = GourmetBurgerSystem(create_menu()) 
      
	def test_refill_inventory(self):
		burger = self.system.new_main_order("base burger")
		burger.add_ingredient("sesame bun", 2, 2)
		burger.add_ingredient("beef patty", 1, 1.5)
		burger.add_ingredient("tomato", 1, 0.5)
		burger.add_ingredient("lettuce", 1, 0.5)
		burger.add_ingredient("cheddar cheese", 1, 0.5)
		burger.add_ingredient("tomato sauce", 1, 0.5)

		wrap = self.system.new_main_order("custom wrap")
		wrap.add_ingredient("white wrap", 1, 1)
		wrap.add_ingredient("tuna filling", 1, 1.5)
		wrap.add_ingredient("tomato", 1, 0.5)   
		wrap.add_ingredient("lettuce", 1, 0.5)
		wrap.add_ingredient("swiss cheese", 1, 0.5)
		wrap.add_ingredient("ians special sauce", 1, 2)

		self.system.place_order([burger])		
		self.system.place_order([wrap])	
