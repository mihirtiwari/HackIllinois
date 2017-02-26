from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import api

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/taken/firstName=<firstName>&lastName=<lastName>', methods=['GET'])
def get_drugs_taken(firstName, lastName):
    drug = api.get_drug(firstName, lastName)
    return jsonify({'drug': drug})

@app.route('/combine/drug=<drug>&check_drug=<check_drug>', methods=['GET'])
def combined_drugs(drug, check_drug):
    meds = []
    meds.append(drug)
    meds.append(check_drug)

    description = api.get_danger(meds)
    return jsonify({'description': description})

if __name__ == "__main__":
    app.run(debug=True)
