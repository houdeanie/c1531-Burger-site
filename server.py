# create the server 
from flask import Flask
from init import bootstrap_system, bootstrap_order

app = Flask(__name__)
app.secret_key = 'very-secret-123'  # Used to add entropy

system = bootstrap_system()
new_order = bootstrap_order()
