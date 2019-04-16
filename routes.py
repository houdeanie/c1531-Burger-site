from flask import render_template, request, redirect, url_for, abort
from server import app, system
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
    new_order = Order()
    system.new_order(new_order)
    if request.method == 'POST':
        if 'checkout_button' in request.form:
            print('checkout')
    return render_template('user_home.html', order=new_order)

'''
Mains page for Gourmet Burgers
create mains
'''
@app.route('/mains', methods=["GET", "POST"])
def mains():
    # takes in order
    
    if request.method == 'POST':
        if 'base_burger' in request.form:
            # add default burger
            return redirect(url_for('main_burger'))
        elif 'custom_burger' in request.form:
            # create burger
            return redirect(url_for('main_wrap'))
        elif 'base_wrap' in request.form:
            # add default wrap
            return redirect(url_for('main_wrap'))
        elif 'custom_wrap' in request.form:
            # create wrap
            return redirect(url_for('main_wrap'))
    return render_template('mains.html')

@app.route('/mains/Burger', methods=["GET", "POST"])
def main_burger():
    if request.method == 'POST':
        # checks for errors
        # if valid
        arr = [] # array size length of items in menu
        if 'order_button' in request.form:
            return redirect(url_for('user_home'))
    return render_template('mains_burger.html')

@app.route('/mains/Wrap', methods=["GET", "POST"])
def main_wrap():
    if request.method == 'POST':
        # checks for errors
        # if valid
        arr = [] # array size length of items in menu
        if 'order_button' in request.form:
            return redirect(url_for('user_home'))
    return render_template('mains_wrap.html')

'''
Sides page for Gourmet Burgers
create sides
'''
@app.route('/sides', methods=["GET", "POST"])
def sides():
    if request.method == 'POST':
        # checks for errors
        # if valid
        arr = [] # array size length of items in menu
        if 'order_button' in request.form:
            # for item in menu
            # find how many items ordered
            # if more than one, add item to order

            return redirect(url_for('user_home'))
    return render_template('sides.html')

'''# for item in menu
            # find how many items ordered
            # if more than one, add item to order
Drinks page for Gourmet Burgers
create drink
'''
@app.route('/drinks', methods=["GET", "POST"])
def drinks():
    if request.method == 'POST':
        # checks for errors
        # if valid
        arr = [] # array size length of items in menu
        if 'order_button' in request.form:
            # for item in menu
            # find how many items ordered
            # if more than one, add item to order
            return redirect(url_for('user_home'))
    return render_template('drinks.html')

'''
Order page for Gourmet Burgers
show customer current order
'''
@app.route('/order', methods=["GET", "POST"])
def user_order():
    return render_template('user_order.html')

'''
Checkout page for Gourmet Burgers
shows order and order id, status. order items, fee 
'''
@app.route('/checkout', methods=["GET", "POST"])
def checkout():

    return render_template('checkout.html')


################# STAFF SIDE ###################


