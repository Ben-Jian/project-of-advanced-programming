import json
import requests

url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-027?Authorization=CWB-951FEBBC-DD1C-49B7-83A0-5525A753D11C"
params = {
  "Authorization": "CWB-951FEBBC-DD1C-49B7-83A0-5525A753D11C",
  "locationName": "斗六市",   #"locationName": "虎尾鎮" also works!!(only shows data of huwei)
}

response = requests.get(url, params=params)
# print(response.status_code)

if response.status_code == 200:
  # print(response.text)
  data = json.loads(response.text)
  print(data)

  location = data["records"]["locations"][0]["location"][0]["locationName"]
  rain_prob=data["records"]["locations"][0]["location"][0]["weatherElement"][0]["time"][0]["elementValue"][0]["value"]
  weather_state=data["records"]["locations"][0]["location"][0]["weatherElement"][1]["time"][2]["elementValue"][0]["value"]
  天氣預報綜合描述=data["records"]["locations"][0]["location"][0]["weatherElement"][6]["time"][2]["elementValue"][0]["value"]
  start_time=data["records"]["locations"][0]["location"][0]["weatherElement"][0]["time"][2]["startTime"]
  end_time=data["records"]["locations"][0]["location"][0]["weatherElement"][0]["time"][2]["endTime"]

  tem_max =data["records"]["locations"][0]["location"][0]["weatherElement"][12]["time"][0]["elementValue"][0]["value"]
  comfort =data["records"]["locations"][0]["location"][0]["weatherElement"][7]["time"][0]["elementValue"][1]["value"]

  print(location)
  print("降雨機率:",rain_prob,"%")
  print(weather_state)
  print(天氣預報綜合描述)
  print(start_time)
  print(end_time)
  # print(weather_state)
  # print(rain_prob)
  print(tem_max)
  print(comfort)
  # print(max_tem)

else:
  print("Can't get data!")
