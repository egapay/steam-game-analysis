import requests
import locale
import pandas as pd

apiEndpoint = "https://steamspy.com/api.php?request=top100forever"

response = requests.get(apiEndpoint)
data = response.json()
# print(json.dumps(data, indent=4))

dataList = []
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

for appid, appInfo in data.items():
    dataList.append({
        "appid":appid,
        "name":appInfo.get("name"),
        "positive":appInfo.get("positive"),
        "negative":appInfo.get("negative"),
        "price":locale.currency(int(appInfo.get("price"))/100),
        "owners":appInfo.get("owners"),
        "averagePlaytime":appInfo.get("average_forever"),
        "medianPlaytime":appInfo.get("median_forever")
    })

df = pd.DataFrame(dataList)
# print(df)

df.to_csv('topgames.csv', index=False)

# df = pd.DataFrame(data)
# df = df[df['name'].notna() & (df['name'] != '')]

# df.to_csv('gamelist.csv', index=False)

