
import pandas as pd

data = [
    {"Name":"A","Sub":"Math","Marks":78,"Age":20},
    {"Name":"B","Sub":"Sci","Marks":85,"Age":21},
    {"Name":"C","Sub":"Math","Marks":90,"Age":22},
    {"Name":"D","Sub":"Sci","Marks":68,"Age":20}
]

df = pd.DataFrame(data)

print(f"Average marks: {df['Marks'].mean()}")

df["Bonus"] = df["Marks"] + 5

print(df[df["Bonus"] >= 85])

topper = df.loc[df["Bonus"].idxmax()]
print("Topper:\n", topper)

sub_avg = df.groupby("Sub")["Marks"].mean()
print("Subject Average:\n", sub_avg)

print(df.sort_values(by="Bonus", ascending=False))
