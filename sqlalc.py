import sqlalchemy
import pandas as pd

server = 'localhost'
database = 'game'
port = 1433
username = 'user'
password = 'user'
table = 'game_data'

engine = sqlalchemy.create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server')
data=pd.DataFrame({
    'appid':[1234, 5678],
    'name':['test game 1', 'test game 2'],
    'positive':[555, 444],
    'negative':[666, 777],
    'price':[9.99, 10.99],
    'owners':[222, 111],
    'average_playtime':[10, 50],
    'median_playtime':[31, 12]
})

try:
    data.to_sql('game_data', con = engine, if_exists='replace', chunksize=1000)

except Exception as e:
    print(f"An error occurred: {e}")