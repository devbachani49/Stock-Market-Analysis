import pandas as pd
df = pd.read_csv("sec_bhavdata_full_04092020.csv", skipinitialspace=True)
df.replace("-", "", inplace=True)
df["CHANGE"] = df["CLOSE_PRICE"]-df["PREV_CLOSE"]
df["DELIV_PER"] = pd.to_numeric(df['DELIV_PER'])
data = df["SYMBOL"][(df.SERIES == "EQ") & (df.DELIV_PER >= 90) & (df["CHANGE"] > 0)]
ndf = pd.DataFrame(data)
ndf.to_csv("SANTANU.csv")
print(data)
# 
