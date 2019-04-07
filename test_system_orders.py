from gourmetBurgerSystem import *
from order import *
from menu import *
from menuItem import *
from errors import OrderError

import pytest

class IdGenerator():
    def __init__(self):
        self._id = 0

    def next(self):
        self._id += 1
        return self._id

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
    # check for valid order (mains)
    def test_main_order(self, sys):
        order = Order()
        burger = sys.get_copy("wrap", 1)
        burger.calc_price()


    # check for valid order (sides)
    def test_sides_order(self, sys):
        order = Order()
    # check for valid order (drinks)
    def test_drinks_order(self,sys):
         order = Order()

    # check invalid orders

    # inventory for an item is too low

    #