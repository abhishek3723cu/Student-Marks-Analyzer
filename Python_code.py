import pandas as pd
import matplotlib.pyplot as plt

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

# 🧾 Bar Chart - Total Marks
plt.figure(figsize=(10,6))
plt.bar(df["Name"],df["Total"], color='skyblue', edgecolor='black')
plt.title("Total Marks of Students")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.xticks(rotation=45)
#plt.grid(axis='y', linestyle='--', alpha=0.7)
#plt.tight_layout()

# Highlight topper
topper_index = df[df["Name"] == topper].index[0]
plt.bar(df["Name"][topper_index], df["Total"][topper_index], color='orange', label=f"Topper: {topper}")
plt.legend()

# Show plot
plt.show()
