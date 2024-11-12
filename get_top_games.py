import requests
import locale
import pandas as pd
import sqlalchemy

apiEndpoint = "https://steamspy.com/api.php?request=top100forever"

server = 'localhost'
database = 'game'
port = 1433
username = 'user'
password = 'user'
table = 'game_data'

engine = sqlalchemy.create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server')

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
        "average_playtime":appInfo.get("average_forever"),
        "median_playtime":appInfo.get("median_forever")
    })

df = pd.DataFrame(dataList)

try:
    df.to_csv('topgames.csv', index=False)
    # Connect to the SQL Server database
    df.to_sql('game_data', con = engine, if_exists='replace', chunksize=1000)

except Exception as e:
    print(f"An error occurred: {e}")