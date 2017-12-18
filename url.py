import requests
import json
import datetime
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=maria+restaurant+ratchaphruek&destinations=Siam+university&traffic_model=best_guess&units=metric&departure_time=now&mode=driving&key=AIzaSyCLg-YW07cR3V8qImanKeJX6KzUM3voXUA'

response=requests.request('GET',url)

data = json.loads(response.text)

now = datetime.datetime.now()

for row in data['rows']:
    for element in row['elements']:
        distance_text = element['distance']
        print ((str((distance_text['value'])/1000)) + ' km')
        duration_in_traffic_text = element['duration_in_traffic']
        print(duration_in_traffic_text['text'])
        print(data['status'])
        print (now.strftime("%Y-%m-%d %H:%M"))

f = open("time_record.txt","a+")
f.write(now.strftime("%Y-%m-%d %H:%M:%S"+","+ duration_in_traffic_text['text'] +","+ data['status'])+"\n")
f.close()
