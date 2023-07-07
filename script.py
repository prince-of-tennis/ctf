from http.client import HTTPSConnection
import json

apiKey = "152d455b3b22482b5ea9"


cellId = 25412872

headers = { "Content-Type" : "application/json" }
conn = HTTPSConnection("apiv2.combain.com")



coord = (32.75532, -117.090011)
conn.request("GET",("/reverse?key="+apiKey+"&lat="+str(coord[0])+"&lon="+str(coord[1])))
response = conn.getresponse()
result = json.load(response)
print(result)


#conn.request("GET", "/reverse?key="+apiKey+"&lat=55.717569&lon=13.213676")

'''
for mcc in range(289,1000):
    data = {
    "radioType": "gsm",
    "cellTowers": [{
        "mobileCountryCode": mcc,
        "cellId": cellId,
        }]
    }
    conn.request("POST", "/?key="+apiKey, json.dumps(data), headers)
    response = conn.getresponse()
    result = json.load(response)
    if ("location" in result):
        print(("Returned location: "+str(result['location']['lat'])+", "+str(result['location']['lng'])))
        print(result)



'''
