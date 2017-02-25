from flask import Flask, jsonify, request
import api

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/taken/<firstName>?<lastName>', methods=['GET'])
def get_drugs_taken(firstName, lastName):
    drug = api.get_drug(firstName, lastName)
    return jsonify({'drug': drug})

# @app.route('/combine', methods=['POST'])
# def combined_drugs():
#


if __name__ == "__main__":
    app.run(debug=True)
