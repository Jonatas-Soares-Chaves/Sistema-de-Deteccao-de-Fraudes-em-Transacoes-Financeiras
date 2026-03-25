import pandas as pd
import os

os.makedirs("data", exist_ok=True)

df = pd.read_csv("data/transacoes.csv")

# limpeza
df.dropna(inplace=True)

# transformação
df["valor"] = df["valor"].astype(float)

df.to_csv("data/transacoes_tratadas.csv", index=False)

print("ETL concluído")