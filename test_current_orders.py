from src.gourmetBurgerSystem import *
from src.menu_creator import *
import pytest

class TestCurrentOrders():
    def setup_method(self):
        self.system = GourmetBurgerSystem(create_menu()) 
	
    def test_empty_current_orders(self):
        current_orders = self.system.get_current_orders()
        assert(current_orders == [])
		
    def test_non_empty_current_orders(self):
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
        current_orders = self.system.get_current_orders()
        assert(len(current_orders) == 1)	
        assert(current_orders[0].items == [burger])
        assert(current_orders[0].status == "preparing")
        assert(current_orders[0].id == 1)
        self.system.place_order([wrap])
        current_orders = self.system.get_current_orders()
        assert(len(current_orders) == 2)	
        assert(current_orders[1].items == [wrap])
        assert(current_orders[1].status == "preparing")
        assert(current_orders[1].id == 2)
        self.system.place_order([burger, wrap])
        current_orders = self.system.get_current_orders()
        assert(len(current_orders) == 3)	
        assert(current_orders[2].items == [burger, wrap])
        assert(current_orders[2].status == "preparing")
        assert(current_orders[2].id == 3)

    def test_successful_update_orders(self):
        burger = self.system.new_main_order("base burger")
        burger.add_ingredient("sesame bun", 2, 2)
        burger.add_ingredient("beef patty", 1, 1.5)
        burger.add_ingredient("tomato", 1, 0.5)
        burger.add_ingredient("lettuce", 1, 0.5)
        burger.add_ingredient("cheddar cheese", 1, 0.5)
        burger.add_ingredient("tomato sauce", 1, 0.5)

        order = Order()
        order = self.system.place_order([burger])	
        current_orders = self.system.get_current_orders() 
        assert(len(current_orders) == 1)      
        self.system.update_order_pickup(1)
        current_orders = self.system.get_current_orders()       
        assert(len(current_orders) == 0)
        assert(order.status == "ready")

		
    def test_check_non_existent_order_id(self):
        try:
            self.system.check_order_status(5)
        except OrderException as err:
            assert(err.message == "order does not exist. Please check order id and try again")
        else: 
            assert(False)
            
    def test_complete_non_existent_order_id(self):
        try:
            self.system.update_order_pickup(5)
        except OrderException as err:
            assert(err.message == "order does not exist. Please check order id and try again")
        else: 
            assert(False)
		
    def test_update_non_existent_order_id(self):
        try:
            self.system.update_order_completed(5)
        except OrderException as err:
            assert(err.message == "order does not exist. Please check order id and try again")
        else: 
            assert(False)
				

				
	

