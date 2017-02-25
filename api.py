import httplib, urllib, base64, json

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Authorization': 'Basic MTdlYmU3MjQzNGE4NDAzOWEwZTQ4OTAwMThiNmM5OTc6OUFBQzI4OThDQUIxMTlCNzlFOTk0NDg5NzBGQzVBMDg3MjlEMTY4RTcyNDk3QzA5MTY2OEE4QjVDQkE2Rjc0RQ=='
}

# params = urllib.urlencode({
#     # Request parameters
# })

body = {
    "Properties": {
        "PatientId": "205028345"
    },
    "Problems": [
        {
            "Code": "1",
            "FreeText": "Heart Attack",
            "Properties": {
                "MyICD10Code": "I21.3"
            }
        },
        {
            "Code": "2",
            "FreeText": "sty"
        }
    ]

}

try:
    conn = httplib.HTTPSConnection('ipl-nonproduction-customer_validation.e-imo.com')
    conn.request("POST", "/api/v3/actions/categorize", str(body), headers)
    response = conn.getresponse()
    data = response.read()
    # j = json.loads(response.text)
    print(data)
    conn.close()
except Exception as e:
    print(e)
