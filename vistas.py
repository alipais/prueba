from flask import render_template
from app import app, obtener_conexion

@app.route('/')
def inicio():
    con, cursor = obtener_conexion()
    cursor.execute('SELECT * FROM usuarios;')
    datos = cursor.fetchall()
    con.close()
    return render_template('./usuarios/usuarios.html', usuarios=datos)
