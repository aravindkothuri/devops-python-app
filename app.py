from flask import Flask, jsonify

app = Flask(__name__)


users = [
    {
        "id": 1,
        "name": "Aravind",
        "role": "DevOps Engineer"
    },
    {
        "id": 2,
        "name": "Rahul",
        "role": "Developer"
    },
    {
        "id": 3,
        "name": "Priya",
        "role": "Tester"
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to DevOps Demo Application",
        "version": "1.0",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })


@app.route("/api/users")
def get_users():
    return jsonify(users)


@app.route("/api/users/<int:user_id>")
def get_user(user_id):

    for user in users:
        if user["id"] == user_id:
            return jsonify(user)

    return jsonify({
        "error": "User not found"
    }), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
