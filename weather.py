import json
import requests

url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-025?Authorization=CWB-951FEBBC-DD1C-49B7-83A0-5525A753D11C&format=JSON&locationName=%E6%96%97%E5%85%AD%E5%B8%82,string&elementName="
params = {
  "Authorization": "CWB-951FEBBC-DD1C-49B7-83A0-5525A753D11C",
  "locationName": "雲林縣",   #"locationName": "虎尾鎮" also works!!(only shows data of huwei)
}

response = requests.get(url, params=params)
# print(response.status_code)

if response.status_code == 200:
  # print(response.text)
  data = json.loads(response.text)
  print(data)

  location = data["records"]["locations"][0]["location"][0]["locationName"]
  # PoP12h=data["records"]["locations"][0]["location"][0]["weatherElement"][0]["description"]
  rain_prob=data["records"]["locations"][0]["location"][0]["weatherElement"][0]["time"][2]["elementValue"][0]["value"]
  weather_state=data["records"]["locations"][0]["location"][0]["weatherElement"][1]["time"][2]["elementValue"][0]["value"]
  天氣預報綜合描述=data["records"]["locations"][0]["location"][0]["weatherElement"][6]["time"][2]["elementValue"][0]["value"]
  start_time=data["records"]["locations"][0]["location"][0]["weatherElement"][0]["time"][2]["startTime"]
  end_time=data["records"]["locations"][0]["location"][0]["weatherElement"][0]["time"][2]["endTime"]

  tem =data["records"]["locations"][0]["location"][0]["weatherElement"][3]["time"][2]["elementValue"][0]["value"]
  comfort =data["records"]["locations"][0]["location"][0]["weatherElement"][5]["time"][0]["elementValue"][1]["value"]
  # max_tem = weatherElement[4]["time"][0]["parameter"]["parameterName"]
  
  # print(PoP12h)
  print(location)
  print("probability of precipitation from 6:00 to 18:00 :",rain_prob,"%")
  print(weather_state)
  print(天氣預報綜合描述)
  print(start_time)
  print(end_time)
  # print(weather_state)
  # print(rain_prob)
  print(tem)
  print(comfort)
  # print(max_tem)

else:
  print("Can't get data!")

