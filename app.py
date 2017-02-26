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
    names = api.get_drug_name(drug)

    code = []
    for n in names:
        c = api.numbers(n)
        code.append(c)

    return jsonify({'num_drugs': len(drug),'drug': drug, 'code': code})

@app.route('/combine/drug=<drug>&check_drug=<check_drug>', methods=['GET'])
def combined_drugs(drug, check_drug):
    meds = parse(drug)
    meds.append(check_drug)

    description = api.get_danger(meds)
    return jsonify({'description': description})

def parse(s):
    split = s.split('/')
    list = []
    for p in split:
        n = ''
        if ',' in p:
            n = p[0:p.index(',')]
        else:
            n = p
            if ' ' in n:
                n = n[0: n.index(' ')]
        list.append(n.lower())

    return list

if __name__ == "__main__":
    app.run(debug=True)
