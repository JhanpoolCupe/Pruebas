import sqlite3

# Crear y conectar a la base de datos simulada
conn = sqlite3.connect(':memory:')  # Usando memoria para simplificar
cursor = conn.cursor()

# Crear una tabla y insertar datos
cursor.execute('''CREATE TABLE market_data (
                    id INTEGER PRIMARY KEY,
                    product TEXT,
                    price REAL)''')

products = [('Gold', 1800.5), ('Oil', 70.3), ('Bitcoin', 30000)]
cursor.executemany('INSERT INTO market_data (product, price) VALUES (?, ?)', products)
conn.commit()

# Función para Immediate-Read (lectura inmediata)
def immediate_read():
    cursor.execute('SELECT * FROM market_data')
    return cursor.fetchall()

# Función para Request-Response (solicitud-respuesta)
def request_response(product_name):
    cursor.execute('SELECT * FROM market_data WHERE product = ?', (product_name,))
    return cursor.fetchone()

# Ejemplo de uso
print("Immediate-Read (Todos los productos):")
all_products = immediate_read()
for product in all_products:
    print(product)

print("\nRequest-Response (Consulta específica):")
requested_product = 'Gold'
product_data = request_response(requested_product)
print(f"Datos de {requested_product}: {product_data}")

# Cerrar la conexión a la base de datos
conn.close()
