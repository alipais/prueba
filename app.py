from flask import Flask, request, jsonify
from componentes.config_db import conexion

app = Flask(__name__)

# Conexión a la base de datos
def obtener_conexion():
    con = conexion
    try:
        cursor = con.cursor(dictionary=True)
        print('Conectada!')
    except Exception as e:
        print(type(e))
        con.connect()
        cursor = con.cursor(dictionary=True)
        print('Reconectada!')
    return con, cursor

# Obtener todos los usuarios
@app.route('/api-favorite_cake/usuarios', methods=['GET'])
def obtener_usuarios():
    con, cursor = obtener_conexion()
    cursor.execute('SELECT * FROM usuarios;')
    datos = cursor.fetchall()
    con.close()
    return jsonify(datos)

# Crear un nuevo usuario
@app.route('/api-favorite_cake/usuarios', methods=['POST'])
def crear_usuario():
    con, cursor = obtener_conexion()
    nuevo_usuario = request.json
    consulta = """
    INSERT INTO usuarios (nombre, apellido, email, contraseña, activo, administrador)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(consulta, (
        nuevo_usuario['nombre'], 
        nuevo_usuario['apellido'], 
        nuevo_usuario['email'], 
        nuevo_usuario['contraseña'], 
        nuevo_usuario['activo'], 
        nuevo_usuario['administrador']
    ))
    con.commit()
    con.close()
    return jsonify({"mensaje": "Usuario creado exitosamente!"}), 201

# Actualizar un usuario existente
@app.route('/api-favorite_cake/usuarios/<int:id_usuario>', methods=['PUT'])
def actualizar_usuario(id_usuario):
    con, cursor = obtener_conexion()
    usuario_actualizado = request.json
    consulta = """
    UPDATE usuarios SET nombre = %s, apellido = %s, email = %s, contraseña = %s, activo = %s, administrador = %s
    WHERE id_usuario = %s
    """
    cursor.execute(consulta, (
        usuario_actualizado['nombre'], 
        usuario_actualizado['apellido'], 
        usuario_actualizado['email'], 
        usuario_actualizado['contraseña'], 
        usuario_actualizado['activo'], 
        usuario_actualizado['administrador'],
        id_usuario
    ))
    con.commit()
    con.close()
    return jsonify({"mensaje": "Usuario actualizado exitosamente!"})

# Eliminar un usuario
@app.route('/api-favorite_cake/usuarios/<int:id_usuario>', methods=['DELETE'])
def eliminar_usuario(id_usuario):
    con, cursor = obtener_conexion()
    consulta = "DELETE FROM usuarios WHERE id_usuario = %s"
    cursor.execute(consulta, (id_usuario,))
    con.commit()
    con.close()
    return jsonify({"mensaje": "Usuario eliminado exitosamente!"})

if __name__ == '__main__':
    app.run(debug=True)
