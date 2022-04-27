import json
from flask import request, jsonify, Blueprint, abort
from my_app import db, app,api
from my_app.product.models import Product
from my_app import db, app, manager
 

 
manager.create_api(Product, methods=['GET', 'POST'])

catalog = Blueprint('catalog', __name__)


 
@catalog.route('/')
@catalog.route('/home')
def home():
    return "Welcome to the Catalog Home."
  
manager.create_api(Product, methods=['GET', 'POST'])



#Customize API
manager.create_api(
    Product,
    methods=['GET', 'POST', 'DELETE'],
    preprocessors={
        'GET_SINGLE': ['a_preprocessor_for_single_get'],
        'GET_MANY': ['another_preprocessor_for_many_get'],
        'POST': ['a_preprocessor_for_post']
    },
    postprocessors={
        'DELETE': ['a_postprocessor_for_delete']
    }
)