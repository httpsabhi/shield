import random

def generate_random_drones():
    return [
        {'id': 1, 'battery': random.randint(10, 100), 'available': True, 'computing_power': random.randint(20, 100), 'location': 'A1'},
        {'id': 2, 'battery': random.randint(10, 100), 'available': True, 'computing_power': random.randint(20, 100), 'location': 'A2'},
        {'id': 3, 'battery': random.randint(10, 100), 'available': False, 'computing_power': random.randint(20, 100), 'location': 'A3'},
        {'id': 4, 'battery': random.randint(10, 100), 'available': True, 'computing_power': random.randint(20, 100), 'location': 'A4'},
    ]