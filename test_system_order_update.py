from src.gourmetBurgerSystem import *
from src.order import *
from src.menu import *
from src.menuItem import *
from src.errors import OrderError

import pytest

@pytest.fixture
def sys():
    system = GourmetBurgerSystem()
    return system

class TestGetOrderStatus():
    def test_get_order_status(self, sys):
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
        order_id = sys.new_order(order)	
        assert(order_id == 1)
        assert(order.get_net_price() == 13.00)
        order_id = sys.new_order(order)	
        assert(order_id == 2)		

class TestCheckStatus():
    def test_check_order_status(self, sys):
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
        order_id = sys.new_order(order)	
        assert(sys.check_order_status(order_id) == "preparing")	
        sys.update_current_order(order_id)
        assert(sys.check_order_status(order_id) == "pickup")
        sys.update_ready_order(order_id)
        assert(sys.check_order_status(order_id) == "Order is not being prepared. Please check order id and try again")

class TestUpdateStatus():
    def test_update_order_status(self, sys): 
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
        order_id = sys.new_order(order)	
        assert(sys.check_order_status(order_id) == "preparing")	
        sys.update_current_order(order_id)
        assert(sys.check_order_status(order_id) == "pickup")

class TestDecInv():
    def test_dec_inventory(self, sys): 	
        sys1 = GourmetBurgerSystem()
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
        order_id = sys.new_order(order)	
        assert(sys.get_menu() == sys1.get_menu())