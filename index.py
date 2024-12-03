import time
import random
import pandas as pd
from flask import Flask, redirect, render_template, request, jsonify, send_file, url_for
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_session import Session
import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash, check_password_hash
import os
from flask import send_from_directory
from flask import Flask, request, jsonify

app = Flask(__name__)

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='terapia_fisica2'
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
    except Error as e:
        print(f"Error: '{e}'")
    return connection

app.secret_key = 'clave_secreta_para_la_sesion'  # Cambia esto por una clave segura
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Actualizar el diccionario de usuarios para almacenar hashes
usuarios = {
    "usuario@example.com": generate_password_hash("12345"),
    "prueba@correo.com": generate_password_hash("contraseña")
}
    
@app.route('/EdicionRegistro')
def EdicionRegistro():
    return render_template('EdicionRegistro.html', current_page='EdicionRegistro')
            
@app.route('/Principal')
def principal():
    return render_template('Home.html')

@app.route('/NuevoRegistro')
def NuevoRegistro():
    return render_template('NuevoRegistro.html', current_page='NuevoRegistro')

@app.route('/Ficha')
def Ficha():
    return render_template('Ficha.html', current_page='Ficha')

@app.route('/MiembroSuperior')
def MiembroSuperior():
    return render_template('MiembroSuperior.html', current_page='MiembroSuperior')

@app.route('/Resumen')
def Resumen():
    return render_template('Resumen.html')

@app.route('/MiembroInferior')
def MiembroInferior():
    return render_template('MiembroInferior.html', current_page='MiembroInferior')

@app.route('/CabezaTorax')
def CabezaTorax():
    return render_template('CabezaTorax.html', current_page='CabezaTorax')

@app.route('/EvaluacionDeLaPostura')
def EvaluacionDeLaPostura():
    return render_template('EvaluacionDeLaPostura.html', current_page='EvaluacionDeLaPostura')

@app.route('/NotasSeguimiento')
def NotasSeguimiento():
    return render_template('NotasSeguimiento.html', current_page='NotasSeguimiento')

@app.route('/PlanDiagnostico')
def PlanDiagnostico():
    return render_template('PlanDiagnostico.html', current_page='PlanDiagnostico')

@app.route('/ConsultaRegistro', methods=['GET'])
def ConsultaRegistro():
    connection = create_connection()
    cursor = connection.cursor()

    # Obtener los folios y nombres para los selectores
    cursor.execute("SELECT DISTINCT folio FROM ficha_identificaciones")
    folios = cursor.fetchall()
    cursor.execute("SELECT DISTINCT nombre_paciente FROM ficha_identificaciones")
    clasificaciones = cursor.fetchall()

    # Obtener los parámetros de filtrado del formulario
    nombre_filtro = request.args.get('nombre')
    folio_filtro = request.args.get('folio')

    # Construir la consulta SQL con filtrado condicional
    sql = "SELECT id, fecha_elaboracion, nombre_paciente, genero, folio FROM ficha_identificaciones WHERE 1=1"
    
    if nombre_filtro:
        sql += " AND nombre_paciente = %s"
    if folio_filtro:
        sql += " AND folio = %s"

    params = []
    if nombre_filtro:
        params.append(nombre_filtro)
    if folio_filtro:
        params.append(folio_filtro)

    cursor.execute(sql, tuple(params))
    registros = cursor.fetchall()

    # Obtener los archivos PDF de las carpetas de los pacientes
    pacientes_pdfs = {}
    for registro in registros:
        paciente_nombre = registro[2]
        folder_path = os.path.join('Pacientes_PDF', paciente_nombre)

        if os.path.exists(folder_path):
            pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]
            pacientes_pdfs[paciente_nombre] = pdf_files

    cursor.close()
    connection.close()

    return render_template('ConsultaRegistro.html', folios=folios, clasificaciones=clasificaciones, registros=registros, pacientes_pdfs=pacientes_pdfs)

@app.route('/descargar_pdf/<nombre_paciente>/<pdf_nombre>')
def descargar_pdf(nombre_paciente, pdf_nombre):
    # Ruta de la carpeta de PDFs
    folder_path = os.path.join('Pacientes_PDF', nombre_paciente)
    
    # Verificar si el archivo PDF existe
    pdf_path = os.path.join(folder_path, pdf_nombre)
    if os.path.exists(pdf_path):
        return send_from_directory(folder_path, pdf_nombre, as_attachment=True)
    else:
        return "Archivo no encontrado", 404

def generar_id_ficha_unico(cursor):
    while True:
        # Obtener los últimos 2 dígitos del año y los 2 dígitos del día
        año = time.strftime("%y")  # Últimos 2 dígitos del año
        dia = time.strftime("%d")   # Día en formato DD

        # Generar un número aleatorio de 2 dígitos
        aleatorio = random.randint(10, 99)

        # Crear el identificador basado en año, día y número aleatorio
        id_ficha = f"{año}{dia}{aleatorio}"

        # Verificar en la base de datos si ya existe
        cursor.execute("SELECT COUNT(*) FROM ficha_identificaciones WHERE id = %s", (id_ficha,))
        if cursor.fetchone()[0] == 0:
            return id_ficha
        
@app.route('/guardar_pdf_Ficha', methods=['POST'])
def guardar_pdf():
    # Obtener el archivo PDF y el nombre del paciente desde el request
    pdf_file = request.files.get('pdf')
    nombre_paciente = request.form.get('nombrePaciente')

    if not pdf_file or not nombre_paciente:
        return jsonify({'message': 'Error: Falta el archivo o el nombre del paciente.'}), 400

    # Ruta base para guardar los archivos
    base_path = 'Pacientes_PDF'

    # Crear la carpeta con el nombre del paciente dentro de la carpeta principal
    paciente_folder = os.path.join(base_path, nombre_paciente)
    
    if not os.path.exists(paciente_folder):
        os.makedirs(paciente_folder)

    # Guardar el PDF en la carpeta del paciente
    pdf_path = os.path.join(paciente_folder, 'Ficha.pdf')
    pdf_file.save(pdf_path)

    return jsonify({'message': f'PDF guardado en: {pdf_path}'}), 200

@app.route('/guardar_pdf_Miembros_Superiores', methods=['POST'])
def guardar_pdf_Miembro_Superior():
    # Obtener el archivo PDF y el nombre del paciente desde el request
    pdf_file = request.files.get('pdf')
    nombre_paciente = request.form.get('nombrePaciente')

    if not pdf_file or not nombre_paciente:
        return jsonify({'message': 'Error: Falta el archivo o el nombre del paciente.'}), 400

    # Ruta base para guardar los archivos
    base_path = 'Pacientes_PDF'

    # Crear la carpeta con el nombre del paciente dentro de la carpeta principal
    paciente_folder = os.path.join(base_path, nombre_paciente)
    
    if not os.path.exists(paciente_folder):
        os.makedirs(paciente_folder)

    # Guardar el PDF en la carpeta del paciente
    pdf_path = os.path.join(paciente_folder, 'Miembros Superiores.pdf')
    pdf_file.save(pdf_path)

    return jsonify({'message': f'PDF guardado en: {pdf_path}'}), 200

@app.route('/guardar_pdf_Miembros_Inferiores', methods=['POST'])
def guardar_pdf_Miembro_Inferior():
    # Obtener el archivo PDF y el nombre del paciente desde el request
    pdf_file = request.files.get('pdf')
    nombre_paciente = request.form.get('nombrePaciente')

    if not pdf_file or not nombre_paciente:
        return jsonify({'message': 'Error: Falta el archivo o el nombre del paciente.'}), 400

    # Ruta base para guardar los archivos
    base_path = 'Pacientes_PDF'

    # Crear la carpeta con el nombre del paciente dentro de la carpeta principal
    paciente_folder = os.path.join(base_path, nombre_paciente)
    
    if not os.path.exists(paciente_folder):
        os.makedirs(paciente_folder)

    # Guardar el PDF en la carpeta del paciente
    pdf_path = os.path.join(paciente_folder, 'Miembros Inferiores.pdf')
    pdf_file.save(pdf_path)

    return jsonify({'message': f'PDF guardado en: {pdf_path}'}), 200

@app.route('/guardar_pdf_Cabeza_y_cuello', methods=['POST'])
def guardar_pdf_Cabeza_y_cuello():
    # Obtener el archivo PDF y el nombre del paciente desde el request
    pdf_file = request.files.get('pdf')
    nombre_paciente = request.form.get('nombrePaciente')

    if not pdf_file or not nombre_paciente:
        return jsonify({'message': 'Error: Falta el archivo o el nombre del paciente.'}), 400

    # Ruta base para guardar los archivos
    base_path = 'Pacientes_PDF'

    # Crear la carpeta con el nombre del paciente dentro de la carpeta principal
    paciente_folder = os.path.join(base_path, nombre_paciente)
    
    if not os.path.exists(paciente_folder):
        os.makedirs(paciente_folder)

    # Guardar el PDF en la carpeta del paciente
    pdf_path = os.path.join(paciente_folder, 'Cabeza y cuello.pdf')
    pdf_file.save(pdf_path)

    return jsonify({'message': f'PDF guardado en: {pdf_path}'}), 200

@app.route('/guardar_pdf_Evaluacion_de_la_postura', methods=['POST'])
def guardar_pdf_Evaluacion_de_la_postura():
    # Obtener el archivo PDF y el nombre del paciente desde el request
    pdf_file = request.files.get('pdf')
    nombre_paciente = request.form.get('nombrePaciente')

    if not pdf_file or not nombre_paciente:
        return jsonify({'message': 'Error: Falta el archivo o el nombre del paciente.'}), 400

    # Ruta base para guardar los archivos
    base_path = 'Pacientes_PDF'

    # Crear la carpeta con el nombre del paciente dentro de la carpeta principal
    paciente_folder = os.path.join(base_path, nombre_paciente)
    
    if not os.path.exists(paciente_folder):
        os.makedirs(paciente_folder)

    # Guardar el PDF en la carpeta del paciente
    pdf_path = os.path.join(paciente_folder, 'Evaluación de la postura.pdf')
    pdf_file.save(pdf_path)

    return jsonify({'message': f'PDF guardado en: {pdf_path}'}), 200

@app.route('/guardar_pdf_Notas_de_seguimiento', methods=['POST'])
def guardar_pdf_Notas_de_seguimiento():
    # Obtener el archivo PDF y el nombre del paciente desde el request
    pdf_file = request.files.get('pdf')
    nombre_paciente = request.form.get('nombrePaciente')

    if not pdf_file or not nombre_paciente:
        return jsonify({'message': 'Error: Falta el archivo o el nombre del paciente.'}), 400

    # Ruta base para guardar los archivos
    base_path = 'Pacientes_PDF'

    # Crear la carpeta con el nombre del paciente dentro de la carpeta principal
    paciente_folder = os.path.join(base_path, nombre_paciente)
    
    if not os.path.exists(paciente_folder):
        os.makedirs(paciente_folder)

    # Guardar el PDF en la carpeta del paciente
    pdf_path = os.path.join(paciente_folder, 'Notas de seguimiento.pdf')
    pdf_file.save(pdf_path)

    return jsonify({'message': f'PDF guardado en: {pdf_path}'}), 200

@app.route('/guardar_pdf_Plan_de_tratamiento', methods=['POST'])
def guardar_pdf_Plan_de_tratamiento():
    # Obtener el archivo PDF y el nombre del paciente desde el request
    pdf_file = request.files.get('pdf')
    nombre_paciente = request.form.get('nombrePaciente')

    if not pdf_file or not nombre_paciente:
        return jsonify({'message': 'Error: Falta el archivo o el nombre del paciente.'}), 400

    # Ruta base para guardar los archivos
    base_path = 'Pacientes_PDF'

    # Crear la carpeta con el nombre del paciente dentro de la carpeta principal
    paciente_folder = os.path.join(base_path, nombre_paciente)
    
    if not os.path.exists(paciente_folder):
        os.makedirs(paciente_folder)

    # Guardar el PDF en la carpeta del paciente
    pdf_path = os.path.join(paciente_folder, 'Plan de tratamiento.pdf')
    pdf_file.save(pdf_path)

    return jsonify({'message': f'PDF guardado en: {pdf_path}'}), 200


@app.route('/guardar_pdf_Notas_de_seguimiento_modificado', methods=['POST'])
def guardar_pdf_Notas_de_seguimiento_modificado():
    # Obtener el archivo PDF y el nombre del paciente desde el request
    pdf_file = request.files.get('pdf')
    nombre_paciente = request.form.get('nombrePaciente')

    if not pdf_file or not nombre_paciente:
        return jsonify({'message': 'Error: Falta el archivo o el nombre del paciente.'}), 400

    # Ruta base para guardar los archivos
    base_path = 'Pacientes_PDF'

    # Crear la carpeta con el nombre del paciente dentro de la carpeta principal
    paciente_folder = os.path.join(base_path, nombre_paciente)
    
    if not os.path.exists(paciente_folder):
        os.makedirs(paciente_folder)

    # Guardar el PDF en la carpeta del paciente
    pdf_path = os.path.join(paciente_folder, 'Notas de seguimiento.pdf')
    pdf_file.save(pdf_path)

    return jsonify({'message': f'PDF guardado en: {pdf_path}'}), 200




















        






# Redirige a la página de inicio de sesión si no se ha iniciado sesión
@app.before_request
def verificar_sesion():
    # Si el usuario no está en la sesión y la URL no es '/login', redirigir al login
    if 'usuario' not in session:
        if request.endpoint not in ['login', 'login_post']:
            return redirect(url_for('login'))
    else:
        # Si el usuario está en sesión, verificar permisos para ciertas rutas
        # Rutas que solo Administradores pueden acceder
        rutas_admin = ['register', 'register_post', 'obtener_usuarios', 'eliminar_usuario', 'roles_counts', 'usuario_info', 'actualizar_usuario']
        if request.endpoint in rutas_admin and session.get('rol') != 1:
            return jsonify({"success": False, "message": "Acceso no autorizado."}), 403

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')  # Asegúrate de que el archivo login.html esté en la carpeta "templates"

@app.route('/login', methods=['POST'])
def login_post():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    connection = create_connection()
    if connection is None:
        return jsonify({"success": False, "message": "Error de conexión a la base de datos."}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        select_query = "SELECT * FROM inicio_sesion WHERE correo_electronico = %s"
        cursor.execute(select_query, (email,))
        user = cursor.fetchone()

        if user and check_password_hash(user['contraseña'], password):
            session['usuario'] = email  # Guardar usuario en la sesión
            session['rol'] = user['rol']  # Guardar rol en la sesión
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": "Correo o contraseña incorrectos."}), 401
    except Error as e:
        print(f"Error al consultar la base de datos: {e}")
        return jsonify({"success": False, "message": "Error interno del servidor."}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('usuario', None)  # Elimina la sesión del usuario
    session.pop('rol', None)      # Elimina el rol del usuario de la sesión
    return redirect(url_for('login'))  # Redirige al login después de cerrar sesión

# Nueva ruta para mostrar el formulario de registro
@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html', current_page='register')  # Asegúrate de que el archivo register.html esté en la carpeta "templates"

# Nueva ruta para manejar el registro de usuarios
@app.route('/register', methods=['POST'])
def register_post():
    try:
        data = request.get_json()
        correo_electronico = data.get('correo_electronico')
        contraseña = data.get('contraseña')
        rol = data.get('rol')

        # Validar que los campos necesarios estén presentes
        if not correo_electronico or not rol:
            return jsonify({"success": False, "message": "Correo electrónico y rol son obligatorios."}), 400

        # Validar que el rol sea 1 o 2
        if rol not in ['1', '2']:
            return jsonify({"success": False, "message": "Rol inválido. Debe ser 1 (Administrador) o 2 (Capturador)."}), 400

        connection = create_connection()
        if connection is None:
            return jsonify({"success": False, "message": "Error de conexión a la base de datos."}), 500

        cursor = connection.cursor(dictionary=True)

        # Contar el número de usuarios por rol
        count_query = "SELECT rol, COUNT(*) as count FROM inicio_sesion GROUP BY rol"
        cursor.execute(count_query)
        counts = cursor.fetchall()

        admin_count = 0
        capturador_count = 0
        for row in counts:
            if row['rol'] == 1:
                admin_count = row['count']
            elif row['rol'] == 2:
                capturador_count = row['count']

        # Verificar límites
        if rol == '1' and admin_count >= 2:
            return jsonify({"success": False, "message": "Ya existen 2 administradores."}), 400
        if rol == '2' and capturador_count >= 10:
            return jsonify({"success": False, "message": "Ya existen 10 capturadores."}), 400

        # Encriptar la contraseña si se proporciona
        if contraseña:
            contraseña_hash = generate_password_hash(contraseña)
        else:
            # Si la contraseña no se proporciona, retornar un error
            return jsonify({"success": False, "message": "La contraseña es obligatoria."}), 400

        # Insertar en la base de datos
        insert_query = """
            INSERT INTO inicio_sesion (correo_electronico, contraseña, rol)
            VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (correo_electronico, contraseña_hash, int(rol)))
        connection.commit()

        # Opcional: Agregar al diccionario de usuarios para login inmediato
        usuarios[correo_electronico] = contraseña_hash  # Almacenar el hash en lugar de la contraseña en texto plano

        return jsonify({"success": True}), 201

    except Error as e:
        print(f"Error al insertar en la base de datos: {e}")
        return jsonify({"success": False, "message": "Error al registrar el usuario."}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    connection = create_connection()
    if connection is None:
        return jsonify({"success": False, "message": "Error de conexión a la base de datos."}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        select_query = "SELECT id, correo_electronico, rol FROM inicio_sesion"
        cursor.execute(select_query)
        usuarios = cursor.fetchall()

        return jsonify(usuarios), 200

    except Error as e:
        print(f"Error al consultar la base de datos: {e}")
        return jsonify({"success": False, "message": "Error interno del servidor."}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    connection = create_connection()
    if connection is None:
        return jsonify({"success": False, "message": "Error de conexión a la base de datos."}), 500

    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM inicio_sesion WHERE id = %s"
        cursor.execute(delete_query, (id,))
        connection.commit()

        return jsonify({"success": True}), 200

    except Error as e:
        print(f"Error al eliminar el usuario: {e}")
        return jsonify({"success": False, "message": "Error al eliminar el usuario."}), 500
    finally:
        cursor.close()
        connection.close()

# Ruta para actualizar usuario
@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.get_json()
    nuevo_correo = data.get('correo_electronico')
    nuevo_rol = data.get('rol')
    nueva_contraseña = data.get('contraseña')  # Nueva contraseña opcional

    # Validar que el correo electrónico y el rol estén presentes
    if not nuevo_correo or not nuevo_rol:
        return jsonify({"success": False, "message": "Correo electrónico y rol son obligatorios."}), 400

    # Validar que el rol sea 1 o 2
    if str(nuevo_rol) not in ['1', '2']:
        return jsonify({"success": False, "message": "Rol inválido. Debe ser 1 (Administrador) o 2 (Capturador)."}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"success": False, "message": "Error de conexión a la base de datos."}), 500

    try:
        cursor = connection.cursor(dictionary=True)

        # Obtener el rol actual del usuario
        select_user_query = "SELECT rol FROM inicio_sesion WHERE id = %s"
        cursor.execute(select_user_query, (id,))
        usuario_actual = cursor.fetchone()

        if not usuario_actual:
            return jsonify({"success": False, "message": "Usuario no encontrado."}), 404

        rol_anterior = usuario_actual['rol']

        # Contar el número de usuarios por rol, excluyendo el usuario que se está actualizando
        count_query = "SELECT rol, COUNT(*) as count FROM inicio_sesion WHERE id != %s GROUP BY rol"
        cursor.execute(count_query, (id,))
        counts = cursor.fetchall()

        admin_count = 0
        capturador_count = 0
        for row in counts:
            if row['rol'] == 1:
                admin_count = row['count']
            elif row['rol'] == 2:
                capturador_count = row['count']

        # Verificar límites si el rol está cambiando
        if nuevo_rol == '1' and admin_count >= 2 and rol_anterior != 1:
            return jsonify({"success": False, "message": "Ya existen 2 administradores."}), 400
        if nuevo_rol == '2' and capturador_count >= 10 and rol_anterior != 2:
            return jsonify({"success": False, "message": "Ya existen 10 capturadores."}), 400

        # Construir la consulta SQL dinámicamente
        if nueva_contraseña and nueva_contraseña.strip() != '':
            # Si se proporciona una nueva contraseña, actualizarla
            contraseña_hash = generate_password_hash(nueva_contraseña)
            update_query = """
                UPDATE inicio_sesion
                SET correo_electronico = %s, rol = %s, contraseña = %s
                WHERE id = %s
            """
            cursor.execute(update_query, (nuevo_correo, int(nuevo_rol), contraseña_hash, id))
        else:
            # Si no se proporciona una nueva contraseña, no actualizarla
            update_query = """
                UPDATE inicio_sesion
                SET correo_electronico = %s, rol = %s
                WHERE id = %s
            """
            cursor.execute(update_query, (nuevo_correo, int(nuevo_rol), id))

        connection.commit()

        return jsonify({"success": True}), 200

    except Error as e:
        print(f"Error al actualizar el usuario: {e}")
        return jsonify({"success": False, "message": "Error al actualizar el usuario."}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/roles/counts', methods=['GET'])
def roles_counts():
    connection = create_connection()
    if connection is None:
        return jsonify({"success": False, "message": "Error de conexión a la base de datos."}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        count_query = "SELECT rol, COUNT(*) as count FROM inicio_sesion GROUP BY rol"
        cursor.execute(count_query)
        counts = cursor.fetchall()

        admin_count = 0
        capturador_count = 0
        for row in counts:
            if row['rol'] == 1:
                admin_count = row['count']
            elif row['rol'] == 2:
                capturador_count = row['count']

        return jsonify({"admin_count": admin_count, "capturador_count": capturador_count}), 200

    except Error as e:
        print(f"Error al consultar la base de datos: {e}")
        return jsonify({"success": False, "message": "Error interno del servidor."}), 500

    finally:
        cursor.close()
        connection.close()

@app.route('/usuario_info', methods=['GET'])
def usuario_info():
    if 'usuario' not in session:
        return jsonify({"success": False, "message": "No autenticado."}), 401

    email = session['usuario']
    rol = session.get('rol')

    return jsonify({
        "correo_electronico": email,
        "rol": rol
    }), 200











        

@app.route('/guardar_datos', methods=['POST'])
def guardar_datos():
    data = request.get_json()

    try:
        connection = create_connection()
        cursor = connection.cursor()

        # Generar id_ficha único de 5 dígitos
        id_ficha = generar_id_ficha_unico(cursor)

        #Inserción en la tabla ficha_identificaciones
        insertar_ficha_identificaciones = """
        INSERT INTO ficha_identificaciones (
            id, fecha_elaboracion, folio, nombre_paciente, genero, fecha_nacimiento, edad, lugar_nacimiento, 
            estado_civil, ocupacion, nacionalidad, domicilio_actual, telefono, contacto_emergencia_nombre, 
            contacto_emergencia_telefono, diagnostico_medico, elaboro_historial_clinico, motivo_consulta
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insertar_ficha_identificaciones, (
            id_ficha,
            data.get('fechaElaboracion'),
            data.get('folio'),
            data.get('nombrePaciente'),
            data.get('sexo'),
            data.get('fechaNacimiento'),
            data.get('edad'),
            data.get('lugarNacimiento'),
            data.get('estadoCivil'),
            data.get('ocupacion'),
            data.get('nacionalidad'),
            data.get('domicilioActual'),
            data.get('telefono'),
            data.get('nombreContactoEmergencia'),
            data.get('telefonoEmergencia'),
            data.get('diagnosticoMedico'),
            data.get('elaboroHistorial'),
            data.get('motivoConsulta')
        ))

        # Inserción en la tabla antecedentespersonalesnopatologicos
        insertar_antecedentes_no_patologicos = """
        INSERT INTO antecedentespersonalesnopatologicos (
            id_ficha, PropiaRenta, Ventilacion, Iluminacion, Piso, Electrodomesticos, Servicios, 
            DescripcionVivienda,
            NoComidasDia, AguaLts, GruposAlimenticios, DescripcionRutinaAlimenticia, 
            HigieneBucal, BanosDia, CambiosRopa, ActividadFisica, Deporte, Ocio, Ocupacion
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insertar_antecedentes_no_patologicos, (
            id_ficha,
            data.get('PropiaRenta'),
            data.get('Ventilacion'),
            data.get('Iluminacion'),
            data.get('Piso'),
            data.get('Electrodomesticos'),
            data.get('Servicios'),
            data.get('DescripcionVivienda'),
            data.get('NoComidasDia'),
            data.get('AguaLts'),
            data.get('GruposAlimenticios'),
            data.get('DescripcionRutinaAlimenticia'),
            data.get('HigieneBucal'),
            data.get('BanosDia'),
            data.get('CambiosRopa'),
            data.get('ActividadFisica'),
            data.get('Deporte'),
            data.get('Ocio'),
            data.get('Ocupacion1')
        ))

        # Inserción en la tabla antecedentesheredofamiliares
        for antecedente in data.get('antecedentes', []):
            insertar_antecedentes_heredofamiliares = """
            INSERT INTO antecedentesheredofamiliares (
                id_ficha, enfermedad, si, no, parentesco, vivo, muerto, otro, observaciones
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insertar_antecedentes_heredofamiliares, (
                id_ficha,
                antecedente.get('enfermedad'),
                antecedente.get('si'),
                antecedente.get('no'),
                antecedente.get('parentesco'),
                antecedente.get('vivo'),
                antecedente.get('muerto'),
                antecedente.get('otro'),
                antecedente.get('observaciones')
            ))

        # Inserción en la tabla antecedentes_patologicos
        for patologia in data.get('datosPatologicos', []):
            insertar_antecedentes_patologicos = """
            INSERT INTO antecedentes_patologicos (
                id_ficha, patologia, si, no, edad_presentacion, secuelas_complicaciones, inmunizaciones, observaciones
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insertar_antecedentes_patologicos, (
                id_ficha,
                patologia.get('patologia'),
                patologia.get('si_pa'),
                patologia.get('no_pa'),
                patologia.get('edad_presento'),
                patologia.get('secuela'),
                patologia.get('inmunizaciones'),
                patologia.get('observaciones1')
            ))

        # Inserción en la tabla antecedentes_ginecobstetricos
        insertar_ginecobstetricos = """
        INSERT INTO antecedentes_ginecobstetricos (
            id_ficha, menarquia, fecha_ultima_menstruacion, caracteristicas_menstruacion, inicio_vida_sexual, 
            uso_anticonceptivos, numero_embarazos, numero_partos, numero_cesareas, observaciones
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insertar_ginecobstetricos, (
            id_ficha,
            data.get('menarquia'),
            data.get('fecha_ultima_menstruacion'),
            data.get('caracteristicas_menstruacion'),
            data.get('inicio_vida_sexual'),
            data.get('uso_anticonceptivos'),
            data.get('numero_embarazos'),
            data.get('numero_partos'),
            data.get('numero_cesareas'),
            data.get('observaciones_gine')
        ))

        # Inserción en la tabla antecedentes_padecimientoactual
        insertar_padecimientoactual = """
        INSERT INTO antecedentes_padecimientoactual (
            id_ficha, descripcion
        ) VALUES (%s, %s)
        """
        cursor.execute(insertar_padecimientoactual, (
            id_ficha,
            data.get('ac_descripcion')
        ))

        # Inserción en la tabla exploracion
        insertar_exploracion = """
        INSERT INTO exploracion (
            id_ficha, habitus_exterior, peso, altura, imc, temperatura, pulso_cardiaco, frecuencia_respiratoria, 
            presion_arterial, saturacion_oxigeno, observaciones, resultados_previos_actuales
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insertar_exploracion, (
            id_ficha,
            data.get('habitus_exterior'),
            data.get('peso'),
            data.get('altura'),
            data.get('imc'),
            data.get('temperatura'),
            data.get('pulso_cardiaco'),
            data.get('frecuencia_respiratoria'),
            data.get('presion_arterial'),
            data.get('saturacion_oxigeno'),
            data.get('observaciones2'),
            data.get('resultados_previos_actuales')
        ))

# -------------------------------------------------------------------------------------------------------------------------------------------------------

        # Inserción en la tabla partes_cuerpo_miembro_superior
        insertar_miembro_superior = """
        INSERT INTO partes_cuerpo_miembro_superior (
            id_ficha, id_partes, observacion, palpacion, descripcion, dolor
        ) VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insertar_miembro_superior, (
            id_ficha,
            1,
            data.get('observacionesMiembrosSuperiores'),
            data.get('palpacionMiembrosSuperiores'),
            data.get('dolorSuperiorMiembrosSuperiores'),
            data.get('dolorexplofisicaMiembrosSuperiores')
        ))

        # Inserción en la tabla fuerza_muscular_miembro_superior
        for movimiento in data.get('fuerzaMuscularMiembrosSuperiores', []):
            insertar_fuerza_muscular = """
            INSERT INTO fuerza_muscular_miembro_superior (
                id_ficha, derecha, movimiento, izquierda
            ) VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insertar_fuerza_muscular, (
                id_ficha,
                movimiento.get('derecho'),
                movimiento.get('movimiento'),
                movimiento.get('izquierdo')
            ))

        # Inserción en la tabla goniometria_miembro_superior
        for goniometria in data.get('goniometriaMiembrosSuperiores', []):
            insertar_goniometria = """
            INSERT INTO goniometria_miembro_superior (
                id_ficha, rango_normal, izquierdo, movimiento, derecho
            ) VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insertar_goniometria, (
                id_ficha,
                goniometria.get('rango'),
                goniometria.get('izquierdo'),
                goniometria.get('movimiento'),
                goniometria.get('derecho')
            ))

        # Inserción en la tabla reflejososteotendinosos_miembro_superior
        for reflejo in data.get('reflejosOsteotendinososMiembrosSuperiores', []):
            insertar_reflejo = """
            INSERT INTO reflejososteotendinosos_miembro_superior (
                id_ficha, izq, rot, der
            ) VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insertar_reflejo, (
                id_ficha,
                reflejo.get('izquierdo'),
                reflejo.get('reflejo'),
                reflejo.get('derecho')
            ))

        # Inserción en la tabla pruebas_evaluaciones_complementarias_miembro_superior
        for prueba in data.get('pruebasEvaluacionesComplementariasMiembrosSuperiores', []):
            insertar_pruebas = """
            INSERT INTO pruebasevaluacionescomplementarias_miembro_superior (
                id_ficha, pruebas, resultadosyanalisis
            ) VALUES (%s, %s, %s)
            """
            cursor.execute(insertar_pruebas, (
                id_ficha,
                prueba.get('prueba'),
                prueba.get('resultado')
            ))

# -------------------------------------------------------------------------------------------------------------------------------------------------------

        # Inserción en la tabla `partes_cuerpo_miembro_inferior`
        cursor.execute("""
            INSERT INTO partes_cuerpo_miembro_inferior (id_ficha, id_partes, observacion, palpacion, descripcion, dolor)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            id_ficha,
            2,
            data.get('observacionesMiembrosInferiores'),
            data.get('palpacionMiembrosInferiores'),
            data.get('dolorSuperiorMiembrosInferiores'),
            data.get('dolorexplofisicaMiembrosInferiores')
        ))

        # Inserción en la tabla `fuerza_muscular_miembro_inferior`
        for movimiento in data.get('fuerzaMuscularMiembrosInferiores', []):
            cursor.execute("""
                INSERT INTO fuerza_muscular_miembro_inferior (id_ficha, derecha, movimiento, izquierda)
                VALUES (%s, %s, %s, %s)
            """, (
                id_ficha,
                movimiento['derecho'],
                movimiento['movimiento'],
                movimiento['izquierdo']
            ))

        # Inserción en la tabla `goniometria_miembro_inferior`
        for goniometria in data.get('goniometriaMiembrosInferiores', []):
            cursor.execute("""
                INSERT INTO goniometria_miembro_inferior (id_ficha, rango_normal, izquierdo, movimiento, derecho)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                id_ficha,
                goniometria['rango'],
                goniometria['izquierdo'],
                goniometria['movimiento'],
                goniometria['derecho']
            ))

        # Inserción en la tabla `reflejososteotendinosos_miembro_inferior`
        for reflejo in data.get('reflejosOsteotendinososMiembrosInferiores', []):
            cursor.execute("""
                INSERT INTO reflejososteotendinosos_miembro_inferior (id_ficha, izq, rot, der)
                VALUES (%s, %s, %s, %s)
            """, (
                id_ficha,
                reflejo['izquierdo'],
                reflejo['reflejo'],
                reflejo['derecho']
            ))

        # Inserción en la tabla `pruebasevaluacionescomplementarias_miembro_inferior`
        for prueba in data.get('pruebasEvaluacionesComplementariasMiembrosInferiores', []):
            cursor.execute("""
                INSERT INTO pruebasevaluacionescomplementarias_miembro_inferior (id_ficha, pruebas, resultadosyanalisis)
                VALUES (%s, %s, %s)
            """, (
                id_ficha,
                prueba['prueba'],
                prueba['resultado']
            ))

        # Inserción en la tabla `ciclo_marcha_miembro_inferior`
        evaluacion_marcha = data.get('evaluacionMarcha', {})
        cursor.execute("""
            INSERT INTO ciclo_marcha_miembro_inferior (id_ficha, fase_apoyo_completo, contacto_talon_izquierdo, contacto_talon_derecho, apoyo_plantar_izquierdo,
                apoyo_plantar_derecho, apoyo_medio_izquierdo, apoyo_medio_derecho, fase_oscilacion_completo, balanceo_inicial_izquierdo,
                balanceo_inicial_derecho, balanceo_medio_izquierdo, balanceo_medio_derecho, balanceo_terminal_izquierdo, balanceo_terminal_derecho,
                rotacion_pelvica_completo, inclinacion_pelvica_completo, flexion_rodilla_izquierdo, flexion_rodilla_derecho, 
                movimientos_coordinados_rodilla_tobillo_izquierdo, movimientos_coordinados_rodilla_tobillo_derecho, 
                movimiento_centro_gravedad_completo, cadencia_completo, balanceo_ms_completo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            id_ficha,
            evaluacion_marcha.get('faseApoyoCompleto'),
            evaluacion_marcha.get('contactoTalonIzquierdo'),
            evaluacion_marcha.get('contactoTalonDerecho'),
            evaluacion_marcha.get('apoyoPlantarIzquierdo'),
            evaluacion_marcha.get('apoyoPlantarDerecho'),
            evaluacion_marcha.get('apoyoMedioIzquierdo'),
            evaluacion_marcha.get('apoyoMedioDerecho'),
            evaluacion_marcha.get('faseOscilacionCompleto'),
            evaluacion_marcha.get('balanceoInicialIzquierdo'),
            evaluacion_marcha.get('balanceoInicialDerecho'),
            evaluacion_marcha.get('balanceoMedioIzquierdo'),
            evaluacion_marcha.get('balanceoMedioDerecho'),
            evaluacion_marcha.get('balanceoTerminalIzquierdo'),
            evaluacion_marcha.get('balanceoTerminalDerecho'),
            evaluacion_marcha.get('rotacionPelvicaCompleto'),
            evaluacion_marcha.get('inclinacionPelvicaCompleto'),
            evaluacion_marcha.get('flexionRodillaIzquierdo'),
            evaluacion_marcha.get('flexionRodillaDerecho'),
            evaluacion_marcha.get('movimientosCoordinadosRodillaTobilloIzquierdo'),
            evaluacion_marcha.get('movimientosCoordinadosRodillaTobilloDerecho'),
            evaluacion_marcha.get('movimientoCentroGravedadCompleto'),
            evaluacion_marcha.get('cadenciaCompleto'),
            evaluacion_marcha.get('balanceoMSCompleto')
        ))    

# -------------------------------------------------------------------------------------------------------------------------------------------------------

        # Inserción en la tabla partes_cuerpo_cabeza_y_torax
        insertar_partes_cuerpo_cabeza_y_torax = """
        INSERT INTO partes_cuerpo_cabeza_y_torax (
            id_ficha, id_partes, observacion, palpacion, descripcion, dolor
        ) VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insertar_partes_cuerpo_cabeza_y_torax, (
            id_ficha,
            3,  # Supongamos que `id_partes` es un valor fijo o lo obtienes de otra forma
            data.get('observacionesCabezaCuello'),
            data.get('palpacionCabezaCuello'),
            data.get('dolorSuperiorCabezaCuello'),
            data.get('dolorexplofisicaCabezaCuello')
        ))

        # Inserción en la tabla fuerza_muscular_cabeza_y_torax
        insertar_fuerza_muscular_cabeza_y_torax = """
        INSERT INTO fuerza_muscular_cabeza_y_torax (
            id_ficha, movimiento, valores_obtenidos
        ) VALUES (%s, %s, %s)
        """
        for movimiento in data.get('fuerzaMuscularCabezaTorax1', []):
            cursor.execute(insertar_fuerza_muscular_cabeza_y_torax, (
                id_ficha,
                movimiento['movimiento'],
                movimiento['valoresObtenidos'],
            ))

        # Inserción en la tabla partes_cuerpo_cabeza_y_torax1
        insertar_partes_cuerpo_cabeza_y_torax1 = """
        INSERT INTO partes_cuerpo_cabeza_y_torax1 (
            id_ficha, id_partes, observacion, palpacion, descripcion, dolor
        ) VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insertar_partes_cuerpo_cabeza_y_torax1, (
            id_ficha,
            4,  # Supongamos que `id_partes` es un valor fijo o lo obtienes de otra forma
            data.get('observacionesColumnaTóraxAbdomen'),
            data.get('palpacionColumnaTóraxAbdomen'),
            data.get('dolorSuperiorColumnaTóraxAbdomen'),
            data.get('dolorexplofisicaColumnaTóraxAbdomen')
        ))

        # Inserción en la tabla fuerza_muscular_cabeza_y_torax1
        insertar_fuerza_muscular_cabeza_y_torax1 = """
        INSERT INTO fuerza_muscular_cabeza_y_torax1 (
            id_ficha, movimiento, valores_obtenidos
        ) VALUES (%s, %s, %s)
        """
        for movimiento in data.get('fuerzaMuscularCabezaTorax2', []):
            cursor.execute(insertar_fuerza_muscular_cabeza_y_torax1, (
                id_ficha,
                movimiento['movimiento'],
                movimiento['valoresObtenidos']
            ))

        # Inserción en la tabla goniometria_cabeza_y_torax
        insertar_goniometria_cabeza_y_torax = """
        INSERT INTO goniometria_cabeza_y_torax (
            id_ficha, rangos_normales, movimientos, resultados
        ) VALUES (%s, %s, %s, %s)
        """
        for goniometria in data.get('goniometriaCabezaTorax', []):
            cursor.execute(insertar_goniometria_cabeza_y_torax, (
                id_ficha,
                goniometria['rango'],
                goniometria['movimiento'],
                goniometria['resultados']
            ))

        # Inserción en la tabla pruebas_evaluaciones_complementarias_cabeza_y_torax
        insertar_pruebas_evaluaciones_complementarias_cabeza_y_torax = """
        INSERT INTO pruebasevaluacionescomplementarias_cabeza_y_torax (
            id_ficha, pruebas, resultadosyanalisis
        ) VALUES (%s, %s, %s)
        """
        for prueba in data.get('pruebasEvaluacionesComplementariasCabezaTorax', []):
            cursor.execute(insertar_pruebas_evaluaciones_complementarias_cabeza_y_torax, (
                id_ficha,
                prueba['prueba'],
                prueba['resultado']
            ))

# -------------------------------------------------------------------------------------------------------------------------------------------------------
        # Inserción en la tabla vistafrontal
        insertar_vista_frontal = """
        INSERT INTO vistafrontal (id_ficha, alineacion_corporal, observaciones)
        VALUES (%s, %s, %s)
        """
        for vista in data.get('vistaFrontal', []):
            cursor.execute(insertar_vista_frontal, (
                id_ficha,
                vista.get('alineacionCorporal'),
                vista.get('ObservacionesvistaFrontal')
            ))

        # Inserción en la tabla vistalateral
        insertar_vista_lateral = """
        INSERT INTO vistalateral (id_ficha, alineacion_corporal, observaciones)
        VALUES (%s, %s, %s)
        """
        for vista in data.get('vistaLateral', []):
            cursor.execute(insertar_vista_lateral, (
                id_ficha,
                vista.get('alineacionCorporal1'),
                vista.get('ObservacionesvistaLateral')
            ))

        # Inserción en la tabla vistaposterior
        insertar_vista_posterior = """
        INSERT INTO vistaposterior (id_ficha, alineacion_corporal, observaciones)
        VALUES (%s, %s, %s)
        """
        for vista in data.get('vistaPosterior', []):
            cursor.execute(insertar_vista_posterior, (
                id_ficha,
                vista.get('alineacionCorporal2'),
                vista.get('ObservacionesvistaPosterior')
            ))

# Insertar los datos en la tabla notas_seguimiento
        datosPrincipal = data.get('principal', {})
        sql = """
        INSERT INTO notas_seguimientos (id_ficha, nombre, diagnostico, folio, fecha, numero_sesion, notas, sugerencias_observaciones, nombreYfirma_tratante)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (
            id_ficha,
            datosPrincipal.get('nombrePaciente_Seguimiento'),
            datosPrincipal.get('diagnostico_Seguimiento'),
            datosPrincipal.get('folio_Seguimiento'),
            datosPrincipal.get('fecha_Seguimiento'),
            datosPrincipal.get('sesion_Seguimiento'),
            datosPrincipal.get('notas_Seguimiento'),
            datosPrincipal.get('sugerencias_Seguimiento'),
            datosPrincipal.get('nombrefirma_Seguimiento')
        )
        cursor.execute(sql, valores)

        # Insertar cada sección adicional
        for seccion in data.get('secciones', []):
            valores_seccion = (
                id_ficha,
                seccion.get('nombrePaciente_Seguimiento'),
                seccion.get('diagnostico_Seguimiento'),
                seccion.get('folio_Seguimiento'),
                seccion.get('fecha_Seguimiento'),
                seccion.get('sesion_Seguimiento'),
                seccion.get('notas_Seguimiento'),
                seccion.get('sugerencias_Seguimiento'),
                seccion.get('nombrefirma_Seguimiento')
            )
            cursor.execute(sql, valores_seccion)

        # Inserción en la tabla plan_tratamientos
        plan_tratamiento = data.get('planTratamiento', [])
        for tratamiento in plan_tratamiento:
            insertar_plan_tratamiento = """
            INSERT INTO plan_tratamientos (
                id_ficha, objetivo, modalidad_terapeutica, descripcion, dosis
            ) VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insertar_plan_tratamiento, (
                id_ficha,
                tratamiento.get('objetivo'),
                tratamiento.get('modalidad'),
                tratamiento.get('descripcion'),
                tratamiento.get('dosis')
            ))        
        
        connection.commit()
        return jsonify({'success': True})
    except Error as e:
        print(f"Error al insertar en la base de datos: {e}")
        return jsonify({'success': False, 'error': str(e)})
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/exportar_excel')
def exportar_excel():
    connection = create_connection()
    cursor = connection.cursor()

    # Ejecutar todas las consultas necesarias y almacenar los resultados en un DataFrame
    queries = [
        "SELECT * FROM ficha_identificaciones",
        "SELECT * FROM antecedentespersonalesnopatologicos",
        "SELECT * FROM antecedentesheredofamiliares",
        "SELECT * FROM antecedentes_patologicos",
        "SELECT * FROM antecedentes_ginecobstetricos",
        "SELECT * FROM antecedentes_padecimientoactual",
        "SELECT * FROM exploracion",
        "SELECT * FROM partes_cuerpo_miembro_superior",
        "SELECT * FROM fuerza_muscular_miembro_superior",
        "SELECT * FROM goniometria_miembro_superior",
        "SELECT * FROM reflejososteotendinosos_miembro_superior",
        "SELECT * FROM pruebasevaluacionescomplementarias_miembro_superior",
        "SELECT * FROM partes_cuerpo_miembro_inferior",
        "SELECT * FROM fuerza_muscular_miembro_inferior",
        "SELECT * FROM goniometria_miembro_inferior",
        "SELECT * FROM reflejososteotendinosos_miembro_inferior",
        "SELECT * FROM pruebasevaluacionescomplementarias_miembro_inferior",
        "SELECT * FROM ciclo_marcha_miembro_inferior",
        "SELECT * FROM partes_cuerpo_cabeza_y_torax",
        "SELECT * FROM fuerza_muscular_cabeza_y_torax",
        "SELECT * FROM partes_cuerpo_cabeza_y_torax1",
        "SELECT * FROM fuerza_muscular_cabeza_y_torax1",
        "SELECT * FROM goniometria_cabeza_y_torax",
        "SELECT * FROM pruebasevaluacionescomplementarias_cabeza_y_torax",
        "SELECT * FROM vistafrontal",
        "SELECT * FROM vistalateral",
        "SELECT * FROM vistaposterior",
        "SELECT * FROM plan_tratamientos",
        "SELECT * FROM notas_seguimientos"
    ]
    
    # Lista para almacenar todos los DataFrames
    dataframes = []
    
    for query in queries:
        cursor.execute(query)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(result, columns=columns)
        
        # Rellenar los valores NaN o vacíos con "No hay información"
        df.fillna("No hay información", inplace=True)
        
        dataframes.append(df)
    
    cursor.close()
    connection.close()
    
    # Combinar todos los DataFrames en un solo archivo Excel con diferentes hojas
    with pd.ExcelWriter('Reporte.xlsx', engine='xlsxwriter') as writer:
        sheet_names = [
            "ficha_identificaciones", "antecedentes_personales", 
            "antecedentes_heredo", "antecedentes_pat",
            "antecedentes_gineco", "antecedentes_padec",
            "exploracion", "partes_cuerpo_sup", 
            "fuerza_muscular_sup", "goniometria_sup", 
            "reflejos_sup", "pruebas_eval_sup", 
            "partes_cuerpo_inf", "fuerza_muscular_inf", 
            "goniometria_inf", "reflejos_inf", 
            "pruebas_eval_inf", "ciclo_marcha_inf",
            "partes_cuerpo_cab", "fuerza_muscular_cab",
            "partes_cuerpo_cab1", "fuerza_muscular_cab1",
            "goniometria_cab", "pruebas_eval_cab",
            "vista_frontal", "vista_lateral", "vista_posterior",
            "plan_tratamientos", "notas_seguimientos"
        ]
        
        for df, sheet in zip(dataframes, sheet_names):
            df.to_excel(writer, sheet_name=sheet, index=False)
            worksheet = writer.sheets[sheet]
            
            # Aplicar formato de tabla
            num_rows, num_cols = df.shape
            worksheet.add_table(0, 0, num_rows, num_cols - 1, {'name': sheet, 'columns': [{'header': col} for col in df.columns], 'autofilter': True})

            # Aplicar formatos específicos
            for col_num, col_name in enumerate(df.columns):
                col_data = df[col_name]
                
                # Determinar el tipo de formato
                if pd.api.types.is_numeric_dtype(col_data):
                    if pd.api.types.is_integer_dtype(col_data):
                        format = writer.book.add_format({'num_format': '0'})  # Enteros
                    elif pd.api.types.is_float_dtype(col_data):
                        format = writer.book.add_format({'num_format': '0.00'})  # Decimales
                elif pd.api.types.is_datetime64_any_dtype(col_data):
                    format = writer.book.add_format({'num_format': 'yyyy-mm-dd'})  # Fechas
                else:
                    format = writer.book.add_format({'text_wrap': True})  # Texto
                
                # Aplicar formato a la columna
                worksheet.set_column(col_num, col_num, None, format)
            
            # Ajustar el ancho de las columnas automáticamente
            for col_num, col_name in enumerate(df.columns):
                column_len = df[col_name].astype(str).map(len).max()
                column_len = max(column_len, len(col_name)) + 2  # Añadir un pequeño margen
                worksheet.set_column(col_num, col_num, column_len)

    # Enviar el archivo al usuario
    return send_file('Reporte.xlsx', as_attachment=True)
          

if __name__ == '__main__':
    app.run(debug=True, port=5020)
