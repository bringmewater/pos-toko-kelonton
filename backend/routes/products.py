from flask import Blueprint, jsonify, request

products_bp = Blueprint('products', __name__)

# In-memory database for demonstration
products = []

# Create a product
@products_bp.route('/', methods=['POST'])
def create_product():
    data = request.json
    new_product = {
        'id': len(products) + 1,
        'name': data['name'],
        'price': data['price'],
        'quantity': data['quantity']
    }
    products.append(new_product)
    return jsonify(new_product), 201

# Read all products
@products_bp.route('/', methods=['GET'])
def get_products():
    return jsonify(products), 200

# Read a specific product
@products_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((prod for prod in products if prod['id'] == product_id), None)
    if product:
        return jsonify(product), 200
    return jsonify({'message': 'Product not found'}), 404

# Update a product
@products_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    product = next((prod for prod in products if prod['id'] == product_id), None)
    if product:
        product['name'] = data.get('name', product['name'])
        product['price'] = data.get('price', product['price'])
        product['quantity'] = data.get('quantity', product['quantity'])
        return jsonify(product), 200
    return jsonify({'message': 'Product not found'}), 404

# Delete a product
@products_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    product = next((prod for prod in products if prod['id'] == product_id), None)
    if product:
        products = [prod for prod in products if prod['id'] != product_id]
        return jsonify({'message': 'Product deleted'}), 200
    return jsonify({'message': 'Product not found'}), 404

