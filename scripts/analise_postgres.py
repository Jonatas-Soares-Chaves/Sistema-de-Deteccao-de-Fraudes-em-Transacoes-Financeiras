import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="fraude_db",
    user="postgres",
    password="1234"
)

query = "SELECT * FROM transacoes WHERE valor > 3000"

df = pd.read_sql(query, conn)

print("Fraudes encontradas:")
print(df.head())

conn.close()