from flask import Flask, jsonify
from faker import Faker

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

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the API!"
    
if __name__ == '__main__':
    app.run(debug=True)
