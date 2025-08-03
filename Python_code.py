import pandas as pd

# Load the Csv file

df = pd.read_csv("data.csv")

#calculate total and avverage marks
df["Total"]= df.iloc[:,1:].sum(axis=1)
df["Average"]=df.iloc[:,1:-1].mean(axis=1)

# Rank students based on total marks
df["Rank"]= df["Total"].rank(ascending=False, method='min').astype(int)

# Sort by rank
df = df.sort_values(by="Rank")

# Identify the topper
topper = df.iloc[0]["Name"]

# Display final table
print("🎓 Student Performance Summary:\n")
print(df.to_string(index=False))
print(f"\n🏆 Topper: {topper}")