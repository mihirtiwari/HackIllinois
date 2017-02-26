from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import api

app = Flask(__name__)
CORS(app)

"""
To ensure our server is working
"""
@app.route('/')
def index():
    return "Hello World!"

"""
GET: Takes the name of the patient and returns the number of drugs being taken,
what drugs are being taken, and the lexographical codes of those drugs
"""
@app.route('/taken/firstName=<firstName>&lastName=<lastName>', methods=['GET'])
def get_drugs_taken(firstName, lastName):
    drug = api.get_drug(firstName, lastName)
    names = api.get_drug_name(drug)

    code = []
    # gets codes for all drugs
    for n in names:
        c = api.numbers(n)
        code.append(c)

    return jsonify({'num_drugs': len(drug),'drug': drug, 'code': code})

"""
GET: Takes all the currently prescribed drugs and the drug that the doctor wants
to prescribe and returns descriptions of their reactions
"""
@app.route('/combine/drug=<drug>&check_drug=<check_drug>', methods=['GET'])
def combined_drugs(drug, check_drug):
    # parses any drug entered and gets a list out of them. The drugs can only
    # have 0s in between and nothing else
    meds = parse(drug)
    meds.append(check_drug)

    description = api.get_danger(meds)
    return jsonify({'description': description})

"""
Parses when multiple drugs are put in with 0s in between each drug
"""
def parse(s):
    split = s.split('0')
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
