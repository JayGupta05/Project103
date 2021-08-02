import pandas as pd
import plotly_express as px

df = pd.read_csv("data.csv")
chart = px.scatter(df, x = "Country", y = "Per capita", size = "Percentage")
chart.show()