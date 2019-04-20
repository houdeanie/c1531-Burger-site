# test.py for testing things
from src.menu import *
from src.gourmetBurgerSystem import GourmetBurgerSystem
from src.order import Order
from src.menu_creator import *
from src.item import *
from src.gourmetBurgerSystem import GourmetBurgerSystem
from src.order import Order
# storing some html code that could be useful for later
# re: iterating through a menus items
'''
{% for item in _menu %}
    <tr>
        <td> {{ item.name}} </td>
        <td> {{ item.price }} </td>
        <td><input name='{{ item.name }}' type="number" min="0"/></td>
    </tr>
{% endfor %}


"burger": Main("burger", 0.0, 1000, "main"), 
"wrap": Main("wrap", 0.0, 1000, "main"), 
"sesame_bun": Ingredient("sesame_bun", 1.00, 1000, "bun"), 
"muffin_bun": Ingredient("muffin_bun", 1.50, 1000, "bun"), 
"beef_patty": Ingredient("beef_patty", 1.5, 1000, "patty"), 
"veg_patty": Ingredient("veg_patty", 1, 1000, "patty"), 
"white_wrap": Ingredient("white_wrap", 1.00, 1000, "wrap"), 
"wholemal_wrap": Ingredient("wholemeal_wrap", 1.00, 1000, "wrap"), 
"tuna_filling": Ingredient("tuna_filling", 1.5, 1000, "filling"), 
"veg_filling": Ingredient("veg_filling", 1.5, 1000, "filling"), 
"tomato": Ingredient("tomato", 0.5, 1000, "ingredient"), 
"lettuce": Ingredient("lettuce", 0.5, 1000, "ingredient"), 
"swiss_cheese": Ingredient("swiss_cheese", 0.5, 1000, "ingredient"), 
"cheddar_cheese": Ingredient("cheddar_cheese", 0.5, 1000, "ingredient"), 
"tomato_sauce": Ingredient("tomato_sauce", 0.5, 1000, "ingredient"), 
"ians_special_sauce": Ingredient("ians_special_sauce", 3.0, 1000, "ingredient"), 
"small_nuggets": Nugget("small_nuggets", 3.0, 10000/3, "side", 3), 
"medium_nuggets": Nugget("medium_nuggets", 5.0, 10000/6, "side", 6), 
"small_fries": Fries("small_fries", 2.5, 10000/75, "side", 75), 
"medium_fries": Fries("medium_fries", 3.5, 10000/150, "side", 150), 
"water": MenuItem("water", 3.0, 1000, "drink"), 
"small_orange_juice": OrangeJuice("small_orange_juice", 2.0, 10000/250, "drink", 250), 
"medium_orange_juice": OrangeJuice("medium_orange_juice", 3.5, 10000/450, "drink", 450)
'''

system = GourmetBurgerSystem(createMenu())

order = Order()

burger = system.new_main_order_item("Burger")

burger.additem

order.add_item()


