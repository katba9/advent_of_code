import pandas as pd
import time

start_time = time.time()

df = pd.read_csv("2024/1st/id.txt", names = ["ids"])
df[["location1", "location2"]] = df["ids"].str.split("   ", expand=True).apply(pd.to_numeric)
df = df.sort_values(by="location1", ascending=True).reset_index()

df2 = pd.DataFrame(df["location2"]).sort_values(by="location2", ascending=True).reset_index()
df2["location1"] = df["location1"]
df2["difference"] = df2["location1"] - df2["location2"]

total = df2['difference'].abs().sum()
list = [n * (df2["location2"].value_counts()[n]) for n in df2["location1"] if n in df2["location2"].values]

print(f"\n\33[42m\n\n    * ❆ ₊˚⋆ Part 1: \33[1m{total} ⋆ ₊* ❅ ˚    \n\033[0m\n\n\33[41m\n\n    * ❆ ₊˚⋆ Part 2: \33[1m{sum(list)} ⋆ ₊* ❅ ˚    \n\033[0m\n")

end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")