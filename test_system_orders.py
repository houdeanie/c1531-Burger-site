from gourmetBurgerSystem import *
from order import *
from menu import *
from menuItem import *

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
    # check for invalid order (empty order)
    def test_empty_order(self, sys):
        
        new_order = sys.new_order()
        assert 

    # check for valid order (mains, sides, drinks)
    def test_full_order(self, sys):

    # check for valid order (mains)
    def test_main_order(self, sys):

    # check for valid order (sides)
    def test_sides_order(self, sys):

    # check for valid order (drinks)
    def test_drinks_order(self,sys):

    

