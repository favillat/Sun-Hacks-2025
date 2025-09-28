import requests, json



def fetch_all_services(SERVICE_ID, OUTFILE):
    BASE_URL = "https://gis.m.asu.edu/server/rest/services/Campus/CampusServices06022023/MapServer/"+ str(SERVICE_ID) +"/query"

    params = {
        "where": "1=1",
        "outFields": "*",
        "f": "pjson", 
        "resultOffset": 0,
        "resultRecordCount": 2000
    }

    r = requests.get(BASE_URL, params=params, timeout=30)
    data = r.json()

    with open(OUTFILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


# Gets Water Filling Stations
fetch_all_services(15, "waterStations.json")
#with open("waterStations.json", 'r', encoding='utf-8') as f:
    #data = json.load(f)
    #features = data['features']
    #for feature in features:
        #buildingName = feature['attributes']['BLDG_NAME']
        #if buildingName is None:
            #print(feature, "\n") 


# Gets Emergency Call Boxes
fetch_all_services(4, "emergencyCallBoxes.json")

# Gets Police Stations
fetch_all_services(11, "policeStations.json")

