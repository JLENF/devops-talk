from flask import Flask, jsonify
from faker import Faker
import socket

app = Flask(__name__)
fake = Faker()

@app.route('/api/users', methods=['GET'])
def get_users():
    users = []
    for _ in range(5):
        user = {
            'username': fake.user_name(),
            'email': fake.email(),
            'is_active': fake.boolean()
        }
        users.append(user)
    return jsonify(users)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    return f'v1.0.6 - Hello from Pod: {hostname}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
