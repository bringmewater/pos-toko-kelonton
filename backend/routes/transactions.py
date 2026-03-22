from flask import Blueprint, request, jsonify

transactions_bp = Blueprint('transactions', __name__)

# Endpoint for sales transactions
@transactions_bp.route('/sales', methods=['POST'])
def sales_transaction():
    data = request.json
    # Here you would process the transaction data
    return jsonify({'message': 'Transaction processed', 'data': data}), 201

# Endpoint for checkout
@transactions_bp.route('/checkout', methods=['POST'])
def checkout():
    data = request.json
    # Here you would process the checkout data
    return jsonify({'message': 'Checkout completed', 'data': data}), 201

