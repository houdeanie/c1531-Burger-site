from flask import render_template, request, redirect, url_for, abort
from server import app, system, new_order
from src.gourmetBurgerSystem import GourmetBurgerSystem
from src.order import Order
# from src.error import OrderError, check_order_error

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
    if len(new_order.items) == 0:
        return render_template('user_home.html')
    else:
        return render_template('user_home.html', order=new_order)

'''
Mains page for Gourmet Burgers
create mains
'''
@app.route('/mains', methods=["GET", "POST"])
def mains():
    if request.method == 'POST':
    #BURGERS
        # add default burger to order, put in all default ingredients and quantities
        if 'base burger' in request.form:
            burger1 = system.display_item('base burger')
            burger2 = system.new_main_order('Base Burger')
            for key, value in burger1.ingredients.items():
                burger2.add_ingredient(key, value, float(value*system.display_inventory.get_price(key)))
            new_order.add_item(burger2, burger2.price)
            return redirect(url_for('user_home'))
        # create customer burger
        elif 'custom burger' in request.form:
            return redirect(url_for('main_burger'))
    # WRAPS
        # add default wrap to order, put in all default ingredients and quantities  
        elif 'base wrap' in request.form:
            wrap1 = system.display_item('base wrap')
            wrap2 = system.new_main_order('Base Wrap')
            for key, value in wrap1.ingredients.items():
                wrap2.add_ingredient(key, value, float(value*system.display_inventory.get_price(key)))
            new_order.add_item(wrap2, wrap2.price)
            return redirect(url_for('user_home'))
        elif 'custom wrap' in request.form:
            return redirect(url_for('main_wrap'))
    return render_template('mains.html', mains=system.display_inventory.get_mains())

@app.route('/mains/Burger', methods=["GET", "POST"])
def main_burger():
    if request.method == 'POST':
        # checks for errors
        # if valid
        quantities = {} # create empty dictionary to store quantities
        if 'order_button' in request.form:
            burger = system.new_main_order('Custom Burger')
            # iterate through to get quantities into array
            for item in system.display_inventory.get_ingredients('burger'):
                if request.form.get(item.name) == '':
                    quantities[item.name] = 0
                else:
                    quantities[item.name] = int(request.form.get(item.name))
            for key, value in quantities.items():
                if value != 0:
                    burger.add_ingredient(key, value, float(value*system.display_inventory.get_price(key)))
            # print(burger)
            new_order.add_item(burger, burger.price)
            return redirect(url_for('user_home'))
    return render_template('mains_burger.html', ingredients=system.display_inventory.get_ingredients("burger"))

@app.route('/mains/Wrap', methods=["GET", "POST"])
def main_wrap():
    if request.method == 'POST':
        # checks for errors
        # if valid
        quantities = {} # create empty dictionary
        if 'order_button' in request.form:
            wrap = system.new_main_order('Custom Wrap')
            for item in system.display_inventory.get_ingredients('wrap'):
                if request.form.get(item.name) == '':
                    quantities[item.name] = 0
                else:
                    quantities[item.name] = int(request.form.get(item.name))
            for key, value in quantities.items():
                if value != 0:
                    wrap.add_ingredient(key, value, float(value*system.display_inventory.get_price(key)))
            # print(burger)
            new_order.add_item(wrap, wrap.price)
            return redirect(url_for('user_home'))
    return render_template('mains_wrap.html', ingredients=system.display_inventory.get_ingredients("wrap"))

'''
Sides page for Gourmet Burgers
create sides
'''
@app.route('/sides', methods=["GET", "POST"])
def sides():
    if request.method == 'POST':
        # checks for errors
        # if valid
        quantities = {} # create empty dictionary
        if 'order_button' in request.form:
            for item in system.display_inventory.get_measured_item('side'):
                if request.form.get(item.name) == '':
                    quantities[item.name] = 0
                else:
                    quantities[item.name] = int(request.form.get(item.name))
            for key, value in quantities.items():
                # print(key, value)
                if value != 0:
                    side = system.display_item(key)
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
        quantities = {} # array size length of items in menu
        if 'order_button' in request.form:
            # drinks = 
            for item in system.display_inventory.get_measured_item('drink'):
                if request.form.get(item.name) == '':
                    quantities[item.name] = 0
                else:
                    quantities[item.name] = int(request.form.get(item.name))
            for key, value in quantities.items():
                if value != 0:
                    drink = system.display_item(key)
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
        quantities = {} # array size length of items in menu
        if 'order_button' in request.form:
            # drinks = 
            for item in system.display_inventory.get_measured_item('dessert'):
                if request.form.get(item.name) == '':
                    quantities[item.name] = 0
                else:
                    quantities[item.name] = int(request.form.get(item.name))
            for key, value in quantities.items():
                if value != 0:
                    dessert = system.display_item(key)
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

    return redirect(url_for('user_home'))

'''
Checkout page for Gourmet Burgers
shows order and order id, status. order items, fee 
'''
@app.route('/checkout', methods=["GET", "POST"])
def checkout():
    order = system.place_order(new_order)
    return render_template('checkout.html', order = order)

'''
Checkout Order page for Gourmet Burgers
show customer current order when given their id
'''
@app.route('/order/<id>', methods=["GET", "POST"])
def checkout_order(order_id):
    order = system._get_order(order_id)
    return render_template('checkout.html', order=order)


################# STAFF SIDE ###################
'''
Staff home page
shows current orders and allows staff to finish orders
finishing an order causes the order to disappear and change order status
'''
@app.route('/staff', methods=["GET", "POST"])
def staff_home():

    return render_template('staff_home.html')

'''
Staff ingredients inventory page
'''
@app.route('/staff/ingredients', methods=["GET", "POST"])
def staff_ingredients():

    return render_template('staff_ingredients.html')

'''
Staff sides inventory page
'''
@app.route('/staff/sides', methods=["GET", "POST"])
def staff_sides():

    return render_template('staff_sides.html')

'''
Staff drinks inventory page
'''
@app.route('/staff/drinks', methods=["GET", "POST"])
def staff_drinks():

    return render_template('staff_drinks.html')

'''
Staff desserts inventory page
'''
@app.route('/staff/desserts', methods=["GET", "POST"])
def staff_desserts():

    return render_template('staff_desserts.html')