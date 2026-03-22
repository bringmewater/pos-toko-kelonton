from flask import Blueprint, request, jsonify

inventory_bp = Blueprint('inventory', __name__)

# Sample inventory data
database = { 'items': [] }

# Endpoint to get inventory items
@inventory_bp.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(database['items']), 200

# Endpoint to add or update inventory items
@inventory_bp.route('/inventory', methods=['POST'])
def add_or_update_inventory():
    new_item = request.json
    # Add or update item logic
    item_id = new_item.get('id')
    if item_id:
        for item in database['items']:
            if item['id'] == item_id:
                item.update(new_item)
                return jsonify(item), 200
        database['items'].append(new_item)
        return jsonify(new_item), 201
    return jsonify({'error': 'ID is required'}), 400

# Endpoint to restock an item
@inventory_bp.route('/inventory/restock', methods=['PUT'])
def restock_item():
    restock_data = request.json
    item_id = restock_data.get('id')
    additional_stock = restock_data.get('amount', 0)
    if item_id:
        for item in database['items']:
            if item['id'] == item_id:
                item['stock'] += additional_stock
                return jsonify(item), 200
        return jsonify({'error': 'Item not found'}), 404
    return jsonify({'error': 'ID is required'}), 400

