import json

def parseJson(data):
    print("Interface Status")
    print("="*80)
    print("DN".ljust(50), "Description".ljust(20), "Speed".ljust(10), "MTU".ljust(10))
    print("-"*50, "-"*20, "-"*10, "-"*10)
    for i in data['imdata']:
        print(i['l1PhysIf']['attributes']['dn'].ljust(50), i['l1PhysIf']['attributes']['descr'].ljust(20), i['l1PhysIf']['attributes']['speed'].ljust(10), i['l1PhysIf']['attributes']['mtu'].ljust(10))

sample = open('/Users/esbolusibaliev/yergali/PP2/Lab4/sample.json', 'r')
data = json.loads(sample.read())
sample.close()

parseJson(data)