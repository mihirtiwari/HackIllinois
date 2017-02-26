import requests, json
import xml.etree.ElementTree as ET

def get_drug(firstName, lastName):
<<<<<<< HEAD
    # headers = {'Accept': 'application/json'}
    # req = requests.get("https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Patient?family=" + lastName + "&given=" + firstName, headers=headers)
    #
    # beginIndex = req.text.find("id") + 5
    # endIndex = req.text.find("care") - 3
    # token = req.text[beginIndex:endIndex]
    #
    # r = requests.get("https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/MedicationOrder?patient=" + token, headers=headers)
    #
    # beginIndex = r.text.find("medicationReference") + 33
    # endIndex = r.text.find("dosageInstruction") - 99
    # string = r.text[beginIndex:endIndex]

=======
    #new medication code
>>>>>>> 18345dc965dd1b2e8aef3cbbc75d32ef10a792c6
    headers = {'Accept': 'application/json'}
    req = requests.get("https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Patient?family=" + lastName + "&given=" + firstName, headers=headers)

    beginIndex = req.text.find("id") + 5
    endIndex = req.text.find("care") - 3
    token = req.text[beginIndex:endIndex]

    response = requests.get("https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/MedicationOrder?patient=" + token, headers=headers)

    json_data = json.loads(response.text)

    array = json_data["entry"]

    meds = []

    for entries in array:
        meds.append(entries["resource"]["medicationReference"]["display"])

    return meds

def get_normid(drug):
    headers = {'Accept': 'application/json'}
    req = requests.get('https://rxnav.nlm.nih.gov/REST/rxcui?name=' + drug, headers)

    root = ET.fromstring(req.text)
    normId = root[0][1].text

    return normId

def get_danger(drugs):
    headers = {'Accept': 'application/json'}
    normOne = get_normid(drugs[0])
    normTwo = get_normid(drugs[1])
    print(normOne)
    req = requests.get('https://rxnav.nlm.nih.gov/REST/interaction/list.json?rxcuis=' + normOne + '+' + normTwo, headers)

    response = req.json()

    interaction = response['fullInteractionTypeGroup'][0]['fullInteractionType']

    interactionPair = interaction[0]['interactionPair'][0]

    description = interactionPair['description']

    return description

def numbers(medication):
    base_url = "http://184.73.124.73:80/PortalWebService/api/v2/product/allergenIT/search"
    headers = {
        'Authorization': "Basic MTdlYmU3MjQzNGE4NDAzOWEwZTQ4OTAwMThiNmM5OTczZTlBQUMyODk4Q0FCMTE5Qjc5RTk5NDQ4OTcwRkM1QTA4NzI5RDE2OEU3MjQ5N0MwOTE2NjhBOEI1Q0JBNkY3NEU=",
        'Content-Type' : 'application/json',
        'Accept': 'application/json'
    }

    theMedication = medication

    body = {
        "searchTerm": theMedication,
        "numberOfResults": 20,
        "dymSize": 0,
        "page": 1,
        "filterByPrecedence": 1,
        "filterByExpression": "",
        "distinctBy": "",
        "properties": "",
        "showFields": "",
        "clientApp": "AMIA Application",
        "clientAppVersion": "1.0",
        "siteId": "Hopspital ABC",
        "userId": "Admin"
    }

    r = requests.post(base_url, headers=headers, json=body)
    code = r.json()["SearchTermResponse"]["items"][0]["code"]

    return code
