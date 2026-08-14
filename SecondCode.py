import pandas as pd

try:
    df = pd.read_csv("dataset/nyc_weather.csv")
    print(df)
except Exception as e:
    print("ERROR:", e)