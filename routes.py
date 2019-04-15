from flask import render_template, request, redirect, url_for, abort
from server import app, system
from src.gourmetBurgerSystem import GourmetBurgerSystem
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
@app.route('/', methods=["GET"])
def user_home():
    # create system
    # create order
    '''
    if 'mains' in request.form:
        return redirect(url_for('mains'))
    elif 'sides' in request.form:
        return redirect(url_for('sides'))
    elif 'drinks' in request.form:
        return redirect(url_for('drinks'))
    '''
    return render_template('user_home.html')

'''
Mains page for Gourmet Burgers
create mains
'''
@app.route('/mains', methods=["GET", "POST"])
def mains():
    
    return render_template('mains.html')

@app.route('/mains/burger', methods=["GET", "POST"])
def main_burger():
    
    return render_template('mains_burger.html')

@app.route('/mains/wrap', methods=["GET", "POST"])
def main_wrap():
    
    return render_template('mains_wrap.html')

'''
Sides page for Gourmet Burgers
create sides
'''
@app.route('/sides', methods=["GET", "POST"])
def sides():
    return render_template('sides.html')

'''
Drinks page for Gourmet Burgers
create drink
'''
@app.route('/drinks', methods=["GET", "POST"])
def drinks():
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


