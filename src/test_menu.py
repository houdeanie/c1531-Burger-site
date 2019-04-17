from menu import *

class TestMenu():
    def setup_method(self):
        self.menu = Menu()

    def test_set_quantity(self):
        #BaseItem
        self.menu.add_base_item("nugget", 0, 1000, "side", ["small nuggets", "medium nuggets", "large nuggets"])
        self.menu.add_measured_item("small nuggets", 3.0, -1, "side", 3, "nuggets") 
        self.menu.add_measured_item("medium nuggets", 5.0, -1, "side", 6, "nuggets")
        self.menu.add_measured_item("large nuggets", 7.0, -1, "side", 10, "nuggets") 
        self.menu.set_quantity("nugget")
        assert(self.menu.get_item("small nuggets").stock_quantity == 1000/3)
        assert(self.menu.get_item("medium nuggets").stock_quantity == 1000/6)        
        assert(self.menu.get_item("large nuggets").stock_quantity == 1000/10)    
        
        #not BaseItem
        assert(self.menu.set_quantity("small nuggets") == False)  

        #item not on menu
        assert(self.menu.set_quantity("fillet o fish") == False)   

        #stock_quantity of base item is 0
        nugget = self.menu.get_item("nugget")
        nugget.stock_quantity = 0
        self.menu.set_quantity("nugget")          
        assert(self.menu.get_item("small nuggets").stock_quantity == 0)
        assert(self.menu.get_item("medium nuggets").stock_quantity == 0)        
        assert(self.menu.get_item("large nuggets").stock_quantity == 0)

        #stock_quantity of base item is < serving_size
        nugget = self.menu.get_item("nugget")
        nugget.stock_quantity = 2
        self.menu.set_quantity("nugget")          
        assert(self.menu.get_item("small nuggets").stock_quantity == 0)
        assert(self.menu.get_item("medium nuggets").stock_quantity == 0)        
        assert(self.menu.get_item("large nuggets").stock_quantity == 0)


