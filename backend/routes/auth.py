from flask import Blueprint, request, jsonify

# Initialize the blueprint
auth_bp = Blueprint('auth', __name__)

# In-memory user storage (for demonstration purposes)
users = {}  

@auth_bp.route('/register', methods=['POST'])
def register():  
    data = request.json  
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({'message': 'User already exists'}), 400  
    users[username] = password  
    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():  
    data = request.json  
    username = data.get('username')
    password = data.get('password')

    if users.get(username) == password:
        return jsonify({'message': 'Login successful'}), 200  
    return jsonify({'message': 'Invalid username or password'}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():  
    # Here you would typically handle session management or token invalidation
    return jsonify({'message': 'Logout successful'}), 200

