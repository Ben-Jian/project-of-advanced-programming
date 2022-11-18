import json
import requests
def get_data():
  url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-027?Authorization=CWB-951FEBBC-DD1C-49B7-83A0-5525A753D11C"
params = {
  "Authorization": "CWB-951FEBBC-DD1C-49B7-83A0-5525A753D11C",
  "locationName": "",   #"locationName": "虎尾鎮" also works!!(only shows data of huwei)
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
  weather_state=data["records"]["locations"][0]["location"][0]["weatherElement"][6]["time"][0]["elementValue"][0]["value"]
  start_time=data["records"]["locations"][0]["location"][0]["weatherElement"][0]["time"][2]["startTime"]
  end_time=data["records"]["locations"][0]["location"][0]["weatherElement"][0]["time"][2]["endTime"]

  max_tem =data["records"]["locations"][0]["location"][0]["weatherElement"][12]["time"][0]["elementValue"][0]["value"]
  comfort =data["records"]["locations"][0]["location"][0]["weatherElement"][7]["time"][0]["elementValue"][1]["value"]
  min_tem = data["records"]["locations"][0]["location"][0]["weatherElement"][8]["time"][0]["elementValue"][0]["value"]
  
#   # print(PoP12h)
#   print(location)
#   print("probability of precipitation from 6:00 to 18:00 :",rain_prob,"%")
#   print(weather_state)
#   print(start_time)
#   print(end_time)
#   # print(weather_state)
#   # print(rain_prob)
#   print(f"max_tem={max_tem}")
#   print(comfort)
#   print(f"min_tem={min_tem}")

else:
  print("Can't get data!")

def line_notify(data):

    # token = "t6eJ17WcGCZ13ZMd9AP6k2hds57HdEqmdZ3yVB1oNuF" #傳給ben
    token ="2w0lbjnDXeVXXfxGWJDy7gqcTyGfXluyM4hd5teH4UW" #傳給line群組
    message = ""

    if len(data) == 0:
        message += "\n[Error] 無法取得天氣資訊"
    else:
      message += f"\n今天{data[0]}的天氣: {data[3]}\n"
      message += f"溫度: {data[5]}°C - {data[7]}°C\n"
      message += f"降雨機率: {data[4]}%\n"
      message += f"舒適度: {data[6]}\n"
      message += f"時間: {data[1]} ~ {data[2]}\n"

    #     message += f"\n今天{data[0]}的天氣: {data[3]}\n"
    #     message += f"溫度: {data[5]}°C\n"
    #     message += f"降雨機率: {data[4]}%\n"
    #     # message += f"舒適度: {data[6]}\n"
    #     message += f"時間: {data[1]} ~ {data[2]}\n"

      if int(data[4]) > 70:
        message += "提醒您，今天很有可能會下雨，出門記得帶把傘哦!"
      elif int(data[5]) > 33:
        message += "提醒您，今天很熱，外出要小心中暑哦~"
      elif int(data[5]) < 10:
        message += "提醒您，今天很冷，記得穿暖一點再出門哦~"

    # line notify所需資料
    line_url = "https://notify-api.line.me/api/notify"
    line_header = {
        "Authorization": 'Bearer ' + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    line_data = {
        "message": message
    }

    requests.post(url=line_url, headers=line_header, data=line_data)

    if __name__ == '__main__':
    
    get_data()
