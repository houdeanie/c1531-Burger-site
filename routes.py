from flask import render_template, request, redirect, url_for, abort
from server import app, system
from src.gourmetBurgers import GourmetBurgerSystem
# from src.error import OrderError, check_order_error

'''
Dedicated page for "page not found"
'''
@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404

'''
Home page for Gourmet Burgers
'''
@app.route('/', methods=["GET", "POST"])
def home():
    return

'''
Mains page for Gourmet Burgers
create mains
'''
@app.route('/mains', methods=["GET", "POST"])
def mains():
    return

'''
Sides page for Gourmet Burgers
create sides
'''
@app.route('/sides', methods=["GET", "POST"])
def sides():
    return


