import mysql.conector

# Conectar a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="usuario",
    password="contraseña",
    database="mi_base_de_datos"
)

# Crear un cursor
cursor = conn.cursor()

# Ejemplo de consulta
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255),
                    email VARCHAR(255))''')

# Insertar datos
cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (%s, %s)", ('Juan', 'juan@example.com'))

# Guardar cambios
conn.commit()

# Cerrar la conexión   
conn.close()
