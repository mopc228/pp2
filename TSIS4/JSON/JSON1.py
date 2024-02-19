import json

file_path = r"C:\Users\kazbe\OneDrive\Desktop\pp2\TSIS4\JSON\sample-data.json"

with open(file_path, "r") as file:
    data = json.load(file)
    for i in data['imdata']:
        print(i['l1PhysIf']['attributes']['dn'],
              i['l1PhysIf']['attributes']['speed'],
              i['l1PhysIf']['attributes']['mtu'],
              sep="  ")
