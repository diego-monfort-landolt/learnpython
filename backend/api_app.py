from flask import Flask, jsonify, request

app = Flask(__name__)

# Beispiel-Daten
users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

@app.route("/")
def home():
    return "Backend läuft!"

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    user = {"id": len(users) + 1, "name": data["name"]}
    users.append(user)
    return jsonify(user), 201

if __name__ == "__main__":
    app.run(debug=True)