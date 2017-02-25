from flask import Flask, jsonify
import api

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/taken', methods=['GET'])
def get_drugs_taken():
    drug = api.get_drug("Jason", "Argonaut")
    return jsonify({'drug': drug})


if __name__ == "__main__":
    app.run(debug=True)
