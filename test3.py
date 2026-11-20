import pandas as pd
import numpy as np

# 1. Read the file
df = pd.read_csv("energy_consumption_forecasting.csv")

# If the file has no header row, give the columns names
if "date" not in df.columns:
    df = pd.read_csv("energy_consumption_forecasting.csv", header=None,
                     names=["date", "day_of_week", "is_weekend", "is_holiday",
                            "avg_temp_c", "humidity_pct", "energy_kwh"])

# 2. Remove duplicates (keep the first one)
df = df.drop_duplicates(subset="date", keep="first")

# 3. Make gender M (only if the file has a gender column)
if "gender" in df.columns:
    df["gender"] = df["gender"].str.strip().str.lower()
    df["gender"] = np.where(df["gender"].isin(["mal4\71e", "m"]), "M", df["gender"])

# 4. Clean day names (sunday -> Sunday)
df["day_of_week"] = df["day_of_week"].str.strip().str.title()

# 5. Fill missing numbers
num_cols = df.select_dtypes(include="number").columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# 6. Save
df.to_csv("updated_file.csv", index=False)
print("Done. Rows saved:", len(df))