import requests, json

# the "Water bottle filling station" layer.
BASE_QUERY_URL = 'https://gis.m.asu.edu/server/rest/services/Campus/CampusServices06022023/MapServer/15/query'
filename = "output.json"

def fetch_all_water():
    offset = 0
    page_size = 2000

    params = {
        "where": "1=1",
        "outFields": "*",
        "f": "pjson", 
        "resultOffset": offset,
        "resultRecordCount": page_size
    }
    r = requests.get(BASE_QUERY_URL, params=params, timeout=30)
    data = r.json()

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    print(f"Fetched {len(data['features'])} records.")

def filter_water():
    fetch_all_water()

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        features = data['features']
        for feature in features:
            buildingName = feature['attributes']['BLDG_NAME']
            if buildingName is None:
                print(feature, "\n") 

    

filter_water()
