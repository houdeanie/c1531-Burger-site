from order import *
from menu import *
from menuItem import *
from gourmetBurgerSystem import *
#test US1 - Customer create main meal 
#(name: String, price: Float, quantity: Int, type: String)
system = GourmetBurgerSystem()
order1 = Order()
burger1 = system.get_copy("burger", 1)
burger1.add_ingredient(system.get_copy("sesame_bun", 2))
print(burger1)
burger1.add_ingredient(system.get_copy("tomato", 1))
burger1.add_ingredient(system.get_copy("swiss_cheese", 1))
burger1.add_ingredient(system.get_copy("beef_patty", 1))
burger1.add_ingredient(system.get_copy("lettuce", 1))
burger1.add_ingredient(system.get_copy("ians_special_sauce", 1))
print(burger1)
burger1.calc_price()
print(burger1.get_price())

drink1 = system.get_copy("small_orange_juice", 1)
print(drink1)
side1 = system.get_copy("small_nuggets", 1)
print(side1)

order1.add_item(burger1)
order1.add_item(drink1)
order1.add_item(side1)
print(order1)
order1.calc_price()
print(order1.get_net_price())

system.new_order(order1)
print(system.show_inventory())



