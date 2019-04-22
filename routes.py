from flask import render_template, request, redirect, url_for, abort
from server import app, system, new_order
from src.gourmetBurgerSystem import GourmetBurgerSystem
from src.order import Order
from src.errors import *

'''
Dedicated page for "page not found"
'''
@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404

################### USER SIDE ######################
'''
Home page for Gourmet Burgers
'''
@app.route('/home', methods=["GET", "POST"])
def user_home():
    if request.method == 'POST':
        if 'reset_order' in request.form:
            new_order.remove_all_items
            return render_template('user_home.html')
    if len(new_order.items) == 0:
        return render_template('user_home.html')
    return render_template('user_home.html', order=new_order)

'''
Mains page for Gourmet Burgers
create mains
'''
@app.route('/mains', methods=["GET", "POST"])
def mains():
    if request.method == 'POST':
        errors = []
    #BURGERS
        # add default burger to order, put in all default ingredients and quantities
        if 'base burger' in request.form:
            burger1 = system.display_item('base burger')
            burger2 = system.new_main_order('Base Burger')
            for key, value in burger1.ingredients.items():
                burger2.add_ingredient(key, value, float(value*system.display_inventory.get_price(key)))
            items = [burger2]
            for item in new_order.items:
                items.append(item)
            # check if item can be added to order
            insufficient = system.check_item_sufficient(items)
            if len(insufficient) == 0:
                new_order.add_item(burger2, burger2.price)
                return redirect(url_for('user_home'))
            else: 
                for key, value in insufficient.items():
                    insufficient_ing_error= str(value) + ' ' + key + 's left'
                    errors.append(insufficient_ing_error)
                errors.append('There are insufficent ingredients in stock to include this item to your current order')
                return render_template('mains.html', mains=system.display_inventory.get_mains(), errors=errors)
        # create custom burger
        elif 'custom burger' in request.form:
            return redirect(url_for('main_burger'))
    # WRAPS
        # add default wrap to order, put in all default ingredients and quantities  
        elif 'base wrap' in request.form:
            wrap1 = system.display_item('base wrap')
            wrap2 = system.new_main_order('Base Wrap')
            for key, value in wrap1.ingredients.items():
                wrap2.add_ingredient(key, value, float(value*system.display_inventory.get_price(key)))
            items = [wrap2]
            for item in new_order.items:
                items.append(item)
            insufficient = system.check_item_sufficient(items)
            if len(insufficient) == 0:
                new_order.add_item(wrap2, wrap2.price)
                return redirect(url_for('user_home'))
            else:
                for key, value in insufficient.items():
                    insufficient_ing_error= str(value) + ' ' + key + 's left'
                    errors.append(insufficient_ing_error)
                errors.append('There are insufficent ingredients in stock to include this item to your current order')
                return render_template('mains.html', mains=system.display_inventory.get_mains(), errors=errors)
        # create custom wrap
        elif 'custom wrap' in request.form:
            return redirect(url_for('main_wrap'))
    return render_template('mains.html', mains=system.display_inventory.get_mains())

@app.route('/mains/Burger', methods=["GET", "POST"])
def main_burger():
    if request.method == 'POST':
        errors = []
        # checks for errors
        quantities = {} # create empty dictionary to store quantities
        if 'order_button' in request.form:
            burger = system.new_main_order('Custom Burger')
            # iterate through to get quantities into array
            for item in system.display_inventory.get_ingredients('burger'):
                if request.form.get(item.name) == '':
                    quantities[item.name] = 0
                else:
                    quantities[item.name] = int(request.form.get(item.name))
            # put quantities of ingredients into burger
            for key, value in quantities.items():
                if value != 0:
                    burger.add_ingredient(key, value, float(value*system.display_inventory.get_price(key)))
            # check if burger is valid
            if check_main_error(burger, 'burger') != None:
                for msg in check_main_error(burger, 'burger'):
                    errors.append(msg)
                return render_template('mains_burger.html', ingredients=system.display_inventory.get_ingredients("burger"), errors=errors)
            # check if burger can be added to order
            items = [burger]
            for item in new_order.items:
                items.append(item)
            insufficient = system.check_item_sufficient(items)
            if len(insufficient) == 0:
                new_order.add_item(burger, burger.price)
                return redirect(url_for('user_home'))
            else:
                for key, value in insufficient.items():
                    insufficient_ing_error= str(value) + ' ' + key + 's left'
                    errors.append(insufficient_ing_error)
                return render_template('mains_burger.html', ingredients=system.display_inventory.get_ingredients("burger"), errors=errors)
    return render_template('mains_burger.html', ingredients=system.display_inventory.get_ingredients("burger"))

@app.route('/mains/Wrap', methods=["GET", "POST"])
def main_wrap():
    if request.method == 'POST':
        errors = []
        # checks for errors
        # if valid
        quantities = {} # create empty dictionary to store quantities
        if 'order_button' in request.form:
            wrap = system.new_main_order('Custom Wrap')
            # iterate through to get quantities into array
            for item in system.display_inventory.get_ingredients('wrap'):
                if request.form.get(item.name) == '':
                    quantities[item.name] = 0
                else:
                    quantities[item.name] = int(request.form.get(item.name))    
            # put quantities of ingredients into wrap
            for key, value in quantities.items():
                if value != 0:
                    wrap.add_ingredient(key, value, float(value*system.display_inventory.get_price(key)))
            # check if wrap is valid
            if check_main_error(wrap, 'wrap') != None:
                for msg in check_main_error(wrap, 'wrap'):
                    errors.append(msg)
                return render_template('mains_wrap.html', ingredients=system.display_inventory.get_ingredients("wrap"), errors=errors)
            # check if wrap can be created
            items = [wrap]
            for item in new_order.items:
                items.append(item)
            insufficient = system.check_item_sufficient(items)
            if len(insufficient) == 0:
                new_order.add_item(wrap, wrap.price)
                return redirect(url_for('user_home'))
            else:
                for key, value in insufficient.items():
                    insufficient_ing_error= str(value) + ' ' + key + 's left'
                    errors.append(insufficient_ing_error)
                return render_template('mains_wrap.html', ingredients=system.display_inventory.get_ingredients("wrap"), errors=errors)
    return render_template('mains_wrap.html', ingredients=system.display_inventory.get_ingredients("wrap"))

'''
Sides page for Gourmet Burgers
create sides
'''
@app.route('/sides', methods=["GET", "POST"])
def sides():
    if request.method == 'POST':
        # checks for errors
        errors = []
        # if valid
        quantities = {} # create empty dictionary
        if 'order_button' in request.form:
            # iterate through to get quantities into array
            for item in system.display_inventory.get_measured_item('side'):
                if request.form.get(item.name) == '':
                    quantities[item.name] = 0
                else:
                    quantities[item.name] = int(request.form.get(item.name))
            # put quantities of ingredients into order, check if quantity can be ordered
            for key, value in quantities.items():
                if value != 0:
                    side = system.display_item(key)
                    items = []
                    for i in range(0, value):   
                        items.append(side)
                    for item in new_order.items:
                        items.append(item)
                    insufficient = system.check_item_sufficient(items)
                    if len(insufficient) != 0:
                        for key, value in insufficient.items():
                            insufficient_ing_error= str(value) + ' ' + key + ' left'
                            errors.append(insufficient_ing_error)
                        return render_template('sides.html', sides=system.display_inventory.get_measured_item('side'), errors=errors)
                    else:
                        for i in range(0, value):
                            new_order.add_item(side, side.price)
            return redirect(url_for('user_home'))
    return render_template('sides.html', sides=system.display_inventory.get_measured_item('side'))

'''
Drinks page for Gourmet Burgers
create drink
'''
@app.route('/drinks', methods=["GET", "POST"])
def drinks():
    if request.method == 'POST':
        # checks for errors
        errors = []
        quantities = {} # array size length of items in menu
        if 'order_button' in request.form:
            # iterate through to get quantities into array
            for item in system.display_inventory.get_measured_item('drink'):
                if request.form.get(item.name) == '':
                    quantities[item.name] = 0
                else:
                    quantities[item.name] = int(request.form.get(item.name))
            # put quantities of ingredients into order
            for key, value in quantities.items():
                if value != 0:
                    drink = system.display_item(key)
                    items = []
                    for i in range(0, value):   
                        items.append(drink)
                    for item in new_order.items:
                        items.append(item)
                    insufficient = system.check_item_sufficient(items)
                    if len(insufficient) != 0:
                        for key, value in insufficient.items():
                            insufficient_ing_error= str(value) + ' ' + key + ' left'
                            errors.append(insufficient_ing_error)
                        return render_template('drinks.html', sides=system.display_inventory.get_measured_item('drinks'), errors=errors)
                    else:
                        for i in range(0, value):
                            new_order.add_item(drink, drink.price)
            return redirect(url_for('user_home'))
    return render_template('drinks.html', drinks=system.display_inventory.get_measured_item('drink'))

'''
Dessert page for Gourmet Burgers
create drink
'''
@app.route('/desserts', methods=["GET", "POST"])
def desserts():
    if request.method == 'POST':
        # checks for errors
        errors = []
        quantities = {} # array size length of items in menu
        if 'order_button' in request.form:
            # iterate through to get quantities into array
            for item in system.display_inventory.get_measured_item('dessert'):
                if request.form.get(item.name) == '':
                    quantities[item.name] = 0
                else:
                    quantities[item.name] = int(request.form.get(item.name))
            # put quantities of ingredients into order
            for key, value in quantities.items():
                if value != 0:
                    dessert = system.display_item(key)
                    items = []
                    for i in range(0, value):   
                        items.append(dessert)
                    for item in new_order.items:
                        items.append(item)
                    insufficient = system.check_item_sufficient(items)
                    if len(insufficient) != 0:
                        for key, value in insufficient.items():
                            insufficient_ing_error= str(value) + ' ' + key + ' left'
                            errors.append(insufficient_ing_error)
                        return render_template('desserts.html', sides=system.display_inventory.get_measured_item('dessert'), errors=errors)
                    else:
                        for i in range(0, value):
                            new_order.add_item(dessert, dessert.price)
            return redirect(url_for('user_home'))
    return render_template('desserts.html', desserts=system.display_inventory.get_measured_item('dessert'))

'''
Order page for Gourmet Burgers
show customer current order
'''
@app.route('/order', methods=["GET", "POST"])
def user_order():
    if request.method == 'POST':
        value = request.form.get('order_id')
        try:
            order_id = int(value)
            order = system.get_order(order_id)
            if order != None:
                return redirect(url_for('checkout_order', order_id = order_id))
            else:
                errors = 'Order with this Order ID does not exist'
                return render_template('user_order.html', errors=errors)
        except ValueError:
            errors = 'Order Id not valid'
            return render_template('user_order.html', errors=errors)
    return render_template('user_order.html')

'''
Checkout page for Gourmet Burgers
shows order and order id, status. order items, fee 
'''
@app.route('/checkout', methods=["GET", "POST"])
def checkout():
    if len(new_order.items) == 0:
        errors = ['Need more than one item to order']
        return redirect(url_for('user_home', errors=errors))
    else:
        # place order 
        order = system.place_order(new_order.items)
        #empty new_order object
        if order != None:
            new_order.remove_all_items
            return render_template('checkout.html', order=order)
        else:
            errors = ['There is a problem with your order, insufficient items in stock to place order']
            return redirect(url_for('user_home', errors = errors))

'''
Checkout Order page for Gourmet Burgers
show customer current order when given their id
'''
@app.route('/order/<order_id>', methods=["GET", "POST"])
def checkout_order(order_id):
    order = system.get_order(order_id)
    return render_template('checkout.html', order=order)


################# STAFF SIDE ###################
'''
Staff home page
shows current orders and allows staff to finish orders
finishing an order causes the order to disappear and change order status
'''
@app.route('/staff', methods=["GET", "POST"])
def staff_home():
    current_orders = system.get_current_orders()
    if request.method == 'POST':
        for order in current_orders:
            if str(order.id) in request.form:
                system.update_order_pickup(order.id)
    return render_template('staff_home.html', current_orders=current_orders)
'''
Staff ingredients inventory page
'''
@app.route('/staff/ingredients', methods=["GET", "POST"])
def staff_ingredients():
    ingredients = system.display_inventory.get_ingredients()
    quantities = {} # dictionary
    if request.method == 'POST':
        if 'refill_button' in request.form:
            for item in ingredients:
                if request.form.get(item.name) == '':
                    quantities[item.name] = 0
                else:
                    quantities[item.name] = int(request.form.get(item.name))
            for key, value in quantities.items():
                ingredient = system.display_item(key)
                ingredient.stock_quantity += value
        quantities.clear()
        return redirect(url_for('staff_ingredients', ingredients=ingredients))
    return render_template('staff_ingredients.html', ingredients=ingredients)

'''
Staff sides inventory page
'''
@app.route('/staff/sides', methods=["GET", "POST"])
def staff_sides():
    # get sides bases
    sides = system.display_inventory.get_measured_item('side')
    base_items = []
    for item in sides:
        base_name = item.base_item
        if system.display_item(base_name) not in base_items:
            base_items.append(system.display_item(base_name))
    # refill quantities
    quantities = {} # dictionary
    if request.method == 'POST':
        # check for errors
        if 'refill_button' in request.form:
            # get refill quantities
            for item in base_items:
                if request.form.get(item.name) == '':
                    quantities[item.name] = 0
                else:
                    quantities[item.name] = int(request.form.get(item.name))
            for key, value in quantities.items():
                base_side = system.display_item(key)
                base_side.stock_quantity += value
        quantities.clear()
        return redirect(url_for('staff_sides', sides=base_items))
    return render_template('staff_sides.html', sides=base_items)

'''
Staff drinks inventory page
'''
@app.route('/staff/drinks', methods=["GET", "POST"])
def staff_drinks():
    drinks = system.display_inventory.get_measured_item('drink')
    base_items = []
    for item in drinks:
        if item.name != 'water':
            base_name = item.base_item
            if system.display_item(base_name) not in base_items:
                base_items.append(system.display_item(base_name))
        else:
            base_items.append(item)
    # refill quantities
    quantities = {}
    if request.method == 'POST':
        # check for errors
        if 'refill_button' in request.form:
            # get refill quantities
            for item in base_items:
                if request.form.get(item.name) == '':
                    quantities[item.name] = 0
                else:
                    quantities[item.name] = int(request.form.get(item.name))
            for key, value in quantities.items():
                base_drink = system.display_item(key)
                base_drink.stock_quantity += value
        quantities.clear()
        return redirect(url_for('staff_drinks', drinks=base_items))
    return render_template('staff_drinks.html', drinks=base_items)

'''
Staff desserts inventory page
'''
@app.route('/staff/desserts', methods=["GET", "POST"])
def staff_desserts():
    desserts = system.display_inventory.get_measured_item('dessert')
    base_items = []
    for item in desserts:
        base_name = item.base_item
        if system.display_item(base_name) not in base_items:
            base_items.append(system.display_item(base_name))
    quantities = {} # dictionary
    if request.method == 'POST':
        # check for errors
        if 'refill_button' in request.form:
            # get refill quantities
            for item in base_items:
                if request.form.get(item.name) == '':
                    quantities[item.name] = 0
                else:
                    quantities[item.name] = int(request.form.get(item.name))
            for key, value in quantities.items():
                base_dessert = system.display_item(key)
                base_dessert.stock_quantity += value
        quantities.clear()
        return redirect(url_for('staff_desserts', desserts=base_items))
    return render_template('staff_desserts.html', desserts=base_items)

'''
chek main item is valid
'''
def check_main_error(item, type):
    errors = []
    # burger must have 2 - 3 buns
    # burger must have no more than 3 patties
    # wrap must have at least 1 wrap
    if type == 'burger':
        total = {'bun': 0, 'patty': 0}
        for key, value in item.ingredients.items():
            ing = system.display_item(key)
            if ing.ing_type == 'bun':
                total['bun']  += value
            if ing.ing_type == 'patty':
                total['patty'] += value
        if total['bun'] < 2 or total['bun'] > 4:
            errors.append('Total buns must be more than or equal to 2 and less than or equal to 4')
        if total['patty'] > 3:
            errors.append('Total patties ust be less than or equal to 3')
        if len(errors) != 0:
            return errors
    elif type == 'wrap':
        ing = item.ingredients
        total = {'wrap': 0}
        for key, value in item.ingredients.items():
            ing = system.display_item(key)
            if ing.ing_type == 'wrap':
                total['wrap']  += value
        if total['wrap'] > 3:
            errors.append('Total wraps must be less that 3')
        if len(errors) != 0:
            return errors
    return None
