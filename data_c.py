
from sklearn.datasets import fetch_california_housing
import pandas as pd

df = fetch_california_housing(as_frame=True).frame
df.to_csv("data/raw_data.csv", index=False)
