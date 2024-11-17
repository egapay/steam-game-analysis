import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

df = pd.read_csv('topgames.csv')

df.plot.scatter(x="positive", y = "price", s=100)