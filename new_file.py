from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Example data to return
    data = {"message": "Hello from the backend!"}
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    # Receive data from the frontend
    content = request.json
    print(content)  # Print the received data to the console
    return jsonify({"status": "success", "received": content}), 201

if __name__ == '__main__':
    app.run(debug=True)