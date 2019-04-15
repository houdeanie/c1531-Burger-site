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
@app.route('/home', methods=["GET"])
def user_home():
    new_order = Order()
    system.new_order(new_order)
    return render_template('user_home.html', order=new_order)

'''
Mains page for Gourmet Burgers
create mains
'''
@app.route('/mains', methods=["GET", "POST"])
def mains():
    # takes in order
    
    #return redirect(url_for('booking_confirm', rego=car.rego, booking=new_booking))
    if request.method == 'POST':
        if 'burger_button' in request.form:
            return redirect(url_for('main_burger'))
        elif 'wrap_button' in request.form:
            return redirect(url_for('main_wrap'))
    return render_template('mains.html')

@app.route('/mains/Burger', methods=["GET", "POST"])
def main_burger():
    if request.method == 'POST':
        # checks for errors
        # if valid
        if 'order_button' in request.form:
            return redirect(url_for('user_home'))
    return render_template('mains_burger.html')

@app.route('/mains/Wrap', methods=["GET", "POST"])
def main_wrap():
    if request.method == 'POST':
        # checks for errors
        # if valid
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
        if 'order_button' in request.form:
            return redirect(url_for('user_home'))
    return render_template('sides.html')

'''
Drinks page for Gourmet Burgers
create drink
'''
@app.route('/drinks', methods=["GET", "POST"])
def drinks():
    if request.method == 'POST':
        # checks for errors
        # if valid
        if 'order_button' in request.form:
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


