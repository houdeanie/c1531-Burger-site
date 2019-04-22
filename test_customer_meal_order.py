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
        wrap = self.system.new_main_order("custom wrap")
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

    def test_ingredient_negative_price(self):
        burger = self.system.new_main_order("custom burger")
        burger.add_ingredient("sesame bun", 2, 2)
        burger.add_ingredient("beef patty", 1, 1.5)
        try:
        	burger.add_ingredient("tomato", 1, -0.5)               
        except OrderException as err:
            assert(err.message == "tomato cannot be free")
        else:
            assert(False)		

    def test_less_than_two_buns(self):
        burger = self.system.new_main_order("custom burger")
        burger.add_ingredient("sesame bun", 1, 2)    
        burger.add_ingredient("beef patty", 1, 1.5)    
        try:
        	self.system.place_order([burger])   
        except OrderException as err:
            assert(err.message == "burger must have at least two buns")
        else:
            assert(False)
		
    def test_greater_than_four_buns(self):
        burger = self.system.new_main_order("custom burger")
        burger.add_ingredient("sesame bun", 5, 2)    
        burger.add_ingredient("beef patty", 1, 1.5)    
        try:
        	self.system.place_order([burger])   
        except OrderException as err:
            assert(err.message == "burger can have maximum 4 buns")
        else:
            assert(False)

    def test_too_many_patties(self):
        burger = self.system.new_main_order("custom burger")
        burger.add_ingredient("sesame bun", 2, 2)  
        burger.add_ingredient("beef patty", 4, 1.5)      
        try:
        	self.system.place_order([burger])   
        except OrderException as err:
            assert(err.message == "burger can have maximum 3 patties")
        else:
            assert(False)

    def test_not_enough_ingredient(self):
        burger = self.system.new_main_order("custom burger")
        burger.add_ingredient("sesame bun", 2, 2)  
        burger.add_ingredient("beef patty", 1, 1.5)     
        burger.add_ingredient("tomato", 5000, 0.5)         
        try:
            self.system.place_order([burger])
        except OrderException as err:
            assert(err.message == "we don't have enough inventory to fulfil this order")
        else: 
            assert(False)

    def test_order_drink(self):
    	self.system.place_order([burger])
        except OrderException as err:
            assert(err.message == "we don't have enough inventory to fulfil this order")
        else: 
            assert(False)
