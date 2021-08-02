import pandas as pd
import plotly_express as px

df = pd.read_csv('data.csv')
chart = px.bar(df,x = 'Country', y = "InternetUsers", color = "Population")
chart.show()