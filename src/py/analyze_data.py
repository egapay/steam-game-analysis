import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

df = pd.read_csv('../csv/topgames.csv')

excluded_columns = ["appid", "name", "owners"]

updated_df = df.drop(columns=excluded_columns)

correlation_df = updated_df.corr()
correlation_long_df = correlation_df.stack().reset_index()
correlation_long_df.columns = ['Var1', 'Var2', 'Correlation']

correlation_long_df.to_csv("../csv/correlation.csv", index=False)