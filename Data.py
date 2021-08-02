import pandas as pd
import plotly.express as px

df = pd.read_csv("data2.csv")
chart = px.line(df, x = "Year", y = "Per capita income", title = "Per Capita Income", color = "Country")
chart.show()