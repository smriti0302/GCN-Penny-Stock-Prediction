import pandas as pd
data = pd.read_excel(r"C:\Users\Sivakumar\Desktop\technology .xlsx")

print(data.columns)
df = data.sort_values(by=['NAME'], ascending=True)
df.to_excel("technology_shareholding_sorted.xlsx")
