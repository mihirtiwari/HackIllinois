import requests, json
import xml.etree.ElementTree as ET

def get_drug(firstName, lastName):
    headers = {'Accept': 'application/json'}
    req = requests.get("https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Patient?family=" + lastName + "&given=" + firstName, headers=headers)

    beginIndex = req.text.find("id") + 5
    endIndex = req.text.find("care") - 3
    token = req.text[beginIndex:endIndex]

    r = requests.get("https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/MedicationOrder?patient=" + token, headers=headers)

    beginIndex = r.text.find("medicationReference") + 33
    endIndex = r.text.find("dosageInstruction") - 99
    string = r.text[beginIndex:endIndex]

    #new medication code
    headers = {'Accept': 'application/json'}
    req = requests.get("https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Patient?family=" + "Argonaut" + "&given=" + "Jason", headers=headers)

    beginIndex = req.text.find("id") + 5
    endIndex = req.text.find("care") - 3
    token = req.text[beginIndex:endIndex]

    response = requests.get("https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/MedicationOrder?patient=" + token, headers=headers)

    json_data = json.loads(response.text)

    array = json_data["entry"]

    for entries in array:
        print(entries["resource"]["medicationReference"]["display"])
    #------------------

    return string

def get_normid(drug):
    headers = {'Accept': 'application/json'}
    drug = drug.lower()
    req = requests.get('https://rxnav.nlm.nih.gov/REST/rxcui?name=' + drug, headers)

    root = ET.fromstring(req.text)
    normId = root[0][1].text

    return normId

def get_danger(drugs):
    headers = {'Accept': 'application/json'}
    req = requests.get('https://rxnav.nlm.nih.gov/REST/interaction/list.json?rxcuis=' + get_normid(drugs[0]) + '+' + get_normid(drugs[1]), headers)

    response = req.json()

    interaction = response['fullInteractionTypeGroup'][0]['fullInteractionType']

    interactionPair = interaction[0]['interactionPair'][0]

    description = interactionPair['description']

    return description
