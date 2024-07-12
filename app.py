from flask import Flask, request, jsonify, render_template
from artifacts.data import generate_random_drones
import random

app = Flask(__name__)

drones = generate_random_drones()

# Function to simulate disaster detection
def detect_disaster():
    return random.choice([True, False])

# Function to select mother drone
def select_mother_drone():
    available_drones = [drone for drone in drones if drone['available']]
    sorted_drones = sorted(available_drones, key=lambda x: (x['battery'], x['computing_power']), reverse=True)
    return sorted_drones[0] if sorted_drones else None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/drones', methods=['GET'])
def get_drones():
    return jsonify(drones)

@app.route('/detect', methods=['GET'])
def disaster_detection():
    if detect_disaster():
        mother_drone = select_mother_drone()
        if mother_drone:
            return jsonify({'message': 'Disaster detected!', 'mother_drone': mother_drone})
        else:
            return jsonify({'message': 'Disaster detected, but no available mother drone!'})
    else:
        return jsonify({'message': 'No disaster detected.'})

@app.route('/report', methods=['POST'])
def report_to_overlord():
    data = request.json
    return jsonify({'message': 'Report received by overlord', 'data': data})

if __name__ == '__main__':
    app.run(debug=True)
