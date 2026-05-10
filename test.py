import pandas as pd

data = {
    "day": ["Monday", "Tuesday", "Wednesday"],
    "sales": [120, 180, 250]
}

df = pd.DataFrame(data)

print(df)
print("\nTotal sales:", df["sales"].sum())