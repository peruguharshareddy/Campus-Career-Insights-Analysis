
import pandas as pd

data = pd.read_csv("../data/placement_data.csv")

# Do not drop rows aggressively
data = data.fillna("None")

data["Placement_Status"] = data["Placed"].apply(lambda x: 1 if x == "Yes" else 0)

data.to_csv("../data/cleaned_data.csv", index=False)

print(data["Placed"].value_counts())
print("Cleaned dataset created successfully")