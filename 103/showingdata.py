import pandas as pd
import plotly.express as px

df = pd.read_csv("coviddata.csv")
figure = px.scatter(df, x="cases", y="date",color="country")
figure.show()
