from gourmetBurgerSystem import *
from order import *
from menu import *
from menuItem import *
from errors import OrderError

import pytest

@pytest.fixture
def sys():
    system = GourmetBurgerSystem()
    return system
    

# check customer can procedurally create an order
class TestCreateOrder():
    # check for empty order
    def test_empty_order(self, sys):
        order = Order()
        try:
            new_order = sys.new_order(order)
        except OrderError as err:
            assert(err.msg == "Must have at least one item in the order")
        # assert len(sys._current_orders) == 0
        # assert sys._current_order == []

    # check for valid order (mains, sides, drinks)
    def test_full_order(self, sys):
        order = Order()
        # create a burger
        burger = sys.get_copy("burger", 1)
        burger.add_ingredient(sys.get_copy("sesame_bun", 2)) # add ingredients, quantity
        burger.add_ingredient(sys.get_copy("tomato", 1))
        burger.add_ingredient(sys.get_copy("swiss_cheese", 1))
        burger.add_ingredient(sys.get_copy("beef_patty", 1))
        burger.add_ingredient(sys.get_copy("lettuce", 1))
        burger.add_ingredient(sys.get_copy("ians_special_sauce", 1))
        burger.calc_price()
        # create drinks and sides
        drink = sys.get_copy("small_orange_juice", 1)
        side = sys.get_copy("small_nuggets", 1)
        order. add_item(burger)
        order.add_item(drink)
        order.add_item(side)
        order.calc_price()
        new_order = sys.new_order(order)

        assert len(sys._current_orders) == 1
        assert sys._current_orders[0] == order
        assert order.get_net_price() == 12.0
        assert order.show_items == sys._current_orders[0].show_items
    # check for valid order (mains) (multiple orders)
    def test_main_order(self, sys):
        order1 = Order()
        order2 = Order()
        wrap = sys.get_copy("wrap", 1)
        wrap.add_ingredient(sys.get_copy("white_wrap", 1))
        wrap.add_ingredient(sys.get_copy("tomato", 1))
        wrap.add_ingredient(sys.get_copy("lettuce", 1))
        wrap.add_ingredient(sys.get_copy("ians_special_sauce", 1))
        wrap.add_ingredient(sys.get_copy("tuna_filling", 1))
        wrap.calc_price()

        burger = sys.get_copy("burger", 1)
        burger.add_ingredient(sys.get_copy("muffin_bun", 2))
        burger.add_ingredient(sys.get_copy("veg_patty", 1))
        burger.add_ingredient(sys.get_copy("beef_patty", 1))
        burger.add_ingredient(sys.get_copy("lettuce", 1))
        burger.add_ingredient(sys.get_copy("cheddar_cheese", 1))
        burger.add_ingredient(sys.get_copy("tomato_sauce", 2))
        burger.calc_price()
        
        order1.add_item(wrap)
        order1.calc_price()
        order2.add_item(burger)
        order2.calc_price()
        new_order1 = sys.new_order(order1)
        new_order2 = sys.new_order(order2)
        assert len(sys._current_orders) == 2
        assert sys._current_orders[0] == order2
        assert sys._current_orders[1] == order1
        assert order1.get_net_price() == 6.5
        assert order2.get_net_price() == 5.5
        assert order2.show_items == sys._current_orders[0].show_items
        assert order1.show_items == sys._current_orders[1].show_items
    # check for valid order (sides)
    def test_sides_order(self, sys):
        order = Order()
        side1 = sys.get_copy("small_nuggets", 1)
        side2 = sys.get_copy("medium_fries", 1)
        order.add_item(side1)
        order.add_item(side2)
        order.calc_price()
        new_order = sys.new_order(order)
        assert len(sys._current_orders) == 1
        assert sys._current_orders[0] == order
        assert order.get_net_price() == 6.5
    # check for valid order (drinks)
    def test_drinks_order(self, sys):
        order = Order()
        drink1 = sys.get_copy("small_orange_juice", 1)
        drink2 = sys.get_copy("medium_orange_juice", 1)
        drink3 = sys.get_copy("water", 1)
        order.add_item(drink1)
        order.add_item(drink2)
        order.add_item(drink3)
        order.calc_price()
        new_order = sys.new_order(order)
        assert len(sys._current_orders) == 1
        assert sys._current_orders[0] == order
        assert order.get_net_price() == 8.5
    
    def test_order_side(self, sys):
        burger = sys.get_copy("burger", 1)
        burger.add_ingredient(sys.get_copy("sesame_bun", 2))
        burger.add_ingredient(sys.get_copy("tomato", 1))		
        burger.add_ingredient(sys.get_copy("swiss_cheese", 1))			
        burger.add_ingredient(sys.get_copy("beef_patty", 1))	
        burger.add_ingredient(sys.get_copy("lettuce", 1))					
        burger.add_ingredient(sys.get_copy("ians_special_sauce", 1))	
        drink = sys.get_copy("small_orange_juice", 1)	
        side = sys.get_copy("small_nuggets", 1)
        order = Order()
        order.add_item(burger)
        order.add_item(drink)
        order.add_item(side)
        new_order = sys.new_order(order)	
        assert sys._current_orders[0] == order

    def test_order_drink(self, sys):	
        burger = sys.get_copy("burger", 1)
        burger.add_ingredient(sys.get_copy("sesame_bun", 2))
        burger.add_ingredient(sys.get_copy("tomato", 1))		
        burger.add_ingredient(sys.get_copy("swiss_cheese", 1))			
        burger.add_ingredient(sys.get_copy("beef_patty", 1))	
        burger.add_ingredient(sys.get_copy("lettuce", 1))					
        burger.add_ingredient(sys.get_copy("ians_special_sauce", 1))	
        drink = sys.get_copy("small_orange_juice", 1)	
        order = Order()
        order.add_item(burger)
        order.add_item(drink)
        new_order = sys.new_order(order)	
        assert sys._current_orders[0] == order

    # check invalid orders
    def test_not_enough_ingredients(self, sys):
        burger = sys.get_copy("burger", 1)
        burger.add_ingredient(sys.get_copy("sesame_bun", 2))	
        burger.add_ingredient(sys.get_copy("beef_patty", 1))	
        burger.add_ingredient(sys.get_copy("lettuce", 10000))	
        order = Order()				
        order.add_item(burger)
        sys.new_order(order)	
        assert len(sys._current_orders) == 1

    def test_not_enough_drink(self, sys): 
        drink = sys.get_copy("small_orange_juice", 10000)	
        order = Order()				
        order.add_item(drink)
        sys.new_order(order)	
        assert len(sys._current_orders) == 1
    
