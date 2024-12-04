import requests
import locale
import pandas as pd
import sqlalchemy
import psycopg2 as pgDB
import os

apiEndpoint = "https://steamspy.com/api.php?request=top100forever"

db_name = os.getenv('DB_NAME')
db_table = os.getenv('DB_TABLE')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')


conn = pgDB.connect(
    database = 'games',
    user = 'postgres',
    password = 'user',
    host = 'localhost',
    port = 5432,
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM public.top_games")

data = cursor.fetchone()
print("DATA: ", data)

conn.close()


# response = requests.get(apiEndpoint)
# data = response.json()

# dataList = []
# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# for appid, appInfo in data.items():
#     dataList.append({
#         "appid":appid,
#         "name":appInfo.get("name"),
#         "positive":appInfo.get("positive"),
#         "positive_percentage": round((appInfo.get("positive") / (appInfo.get("positive") + appInfo.get("negative")) * 100), 2),
#         "negative":appInfo.get("negative"),
#         "negative_percentage": round((appInfo.get("negative") / (appInfo.get("positive") + appInfo.get("negative")) * 100), 2),
#         "total_reviews": appInfo.get("positive") + appInfo.get("negative"),
#         "price":int(appInfo.get("price"))/100,
#         "owners":appInfo.get("owners"),
#         "average_playtime_hours": round((appInfo.get("average_forever") / 60), 0),
#         "median_playtime_hours": round((appInfo.get("median_forever") / 60), 0),
#     })

# df = pd.DataFrame(dataList)

# try:
#     df.to_csv('topgames.csv', index=False)
#     # Connect to the SQL Server database
#     df.to_sql('game_data', con = engine, if_exists='replace', chunksize=1000)

# except Exception as e:
#     print(f"An error occurred: {e}")