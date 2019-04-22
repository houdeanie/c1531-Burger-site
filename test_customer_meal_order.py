from src.gourmetBurgerSystem import *
from src.menu_creator import *
import pytest

class TestCreateMain():
    def setup_method(self):
        self.system = GourmetBurgerSystem(create_menu())

    def test_successful_burger_order(self):
        burger = self.system.new_main_order("custom burger")
        burger.add_ingredient("sesame bun", 2, 2)
        burger.add_ingredient("beef patty", 1, 1.5)
        burger.add_ingredient("tomato", 1, 0.5)
        burger.add_ingredient("lettuce", 1, 0.5)
        burger.add_ingredient("cheddar cheese", 1, 0.5)
        burger.add_ingredient("tomato sauce", 1, 0.5)
        self.system.place_order([burger])
        assert(len(self.system._order_history) == 1)
        assert(self.system._order_history[0].items == [burger])


    def test_successful_wrap_order(self):
        wrap = self.system.new_main_order("custom burger")
        wrap.add_ingredient("white wrap", 1, 1)
        wrap.add_ingredient("tuna filling", 1, 1.5)
        wrap.add_ingredient("tomato", 1, 0.5)   
        wrap.add_ingredient("lettuce", 1, 0.5)
        wrap.add_ingredient("swiss cheese", 1, 0.5)
        wrap.add_ingredient("ians special sauce", 1, 2)
        self.system.place_order([wrap])
        assert(len(self.system._order_history) == 1)
        assert(self.system._order_history[0].items == [wrap])
		
    def test_non_existent_ingredient(self):
        burger = self.system.new_main_order("custom burger")
        burger.add_ingredient("sesame bun", 2, 2)
        burger.add_ingredient("beef patty", 1, 1.5)
        burger.add_ingredient("tommmato", 1, 0.5)
        try:
            self.system.place_order([burger])
        except OrderException as err:
            assert(err.message == "tommmato is not a valid ingredient")
        else:
            assert(False)
#    def test_ingredient_negative_price(self):
               
		
#    def test_less_than_two_buns(self):
#        pass	
		
#    def test_greater_than_four_buns(self):
#        pass
	
#	def test_zero_or_less_patties(self):
#		pass
		
#	def test_too_many_patties(self):
#		pass	
		
#	def test_not_enough_burger_ingredients(self):
#		pass
		
#	def test_not_enough_wrap_ingredients(self):
#		pass
		
#	def test_multiple_burgers(self):
#		pass
		
#	def test_multiple_wraps(self):
#		pass
		
#	def test_multiple_same_ingredient(self):
#		pass
		
#	def test_remove_ingredient(self):
#		pass
		
#	def test_remove_all_ingredients(self):
#		pass
		
#	def test_add_non_ingredient(self):
#		pass
		
#	def test_no_bun_no_patty_burger(self):
#		pass
		
