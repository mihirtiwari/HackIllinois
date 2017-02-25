import requests, json

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

    return string
