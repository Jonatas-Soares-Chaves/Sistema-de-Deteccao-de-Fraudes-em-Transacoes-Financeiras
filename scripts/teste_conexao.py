import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="fraude_db",
        user="postgres",
        password="1234",
        port="5432"
    )

    print("✅ Conectado com sucesso ao PostgreSQL!")

    conn.close()

except Exception as e:
    print("❌ Erro ao conectar:")
    print(e)