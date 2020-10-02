import requests
import pandas as pd

url = "http://api.bcb.gov.br/dados/serie/bcdata.sgs.16121/dados?formato=json"
response = requests.get(url)
response.headers 
response.json()
df = pd.json_normalize(response.json())
df_copy = df.copy()
df_copy.data = pd.to_datetime(df_copy['data']) #Now we have a data column
df_copy.valor = pd.to_numeric(df_copy['valor'])
df_new = df_copy.groupby(pd.Grouper(key="data", freq="1Y")).mean() #Now we get the monthly mean

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
sns.lineplot(x='data',y='valor',data=df_new)
