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


# Ruta para consultar los datos por ID
@app.route('/consultar', methods=['POST'])
def consultar():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)

        # Consulta a ficha_identificaciones
        query1 = """
        SELECT id, fecha_elaboracion, folio, nombre_paciente, genero, fecha_nacimiento, edad, lugar_nacimiento, 
               estado_civil, ocupacion, nacionalidad, domicilio_actual, telefono, contacto_emergencia_nombre, 
               contacto_emergencia_telefono, diagnostico_medico, elaboro_historial_clinico, motivo_consulta
        FROM ficha_identificaciones
        WHERE id = %s
        """
        cursor.execute(query1, (id_recibido,))
        result1 = cursor.fetchone()

        # Consulta a antecedentespersonalesnopatologicos
        query2 = """
        SELECT id_ficha, PropiaRenta, Ventilacion, Iluminacion, Piso, Electrodomesticos, Servicios, 
               DescripcionVivienda, NoComidasDia, AguaLts, GruposAlimenticios, DescripcionRutinaAlimenticia, 
               HigieneBucal, BanosDia, CambiosRopa, ActividadFisica, Deporte, Ocio, Ocupacion
        FROM antecedentespersonalesnopatologicos
        WHERE id_ficha = %s
        """
        cursor.execute(query2, (id_recibido,))
        result2 = cursor.fetchone()

        if result1 or result2:
            # Combinar los resultados de ambas consultas
            combined_result = {}
            if result1:
                combined_result.update(result1)
            if result2:
                combined_result.update(result2)
            return jsonify(combined_result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarAntecedentesHeredoFamiliares', methods=['POST'])
def consultar_antecedentes_heredo_familiares():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            enfermedad, si, no, parentesco, vivo, muerto, otro, observaciones
        FROM antecedentesheredofamiliares
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchall()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarAntecedentesPatologicos', methods=['POST'])
def consultar_antecedentes_patologicos():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            patologia, si, no, edad_presentacion, secuelas_complicaciones, inmunizaciones, observaciones
        FROM antecedentes_patologicos
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchall()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarAntecedentesGinecobstetricos', methods=['POST'])
def consultar_antecedentes_ginecobstetricos():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            menarquia, fecha_ultima_menstruacion, caracteristicas_menstruacion, inicio_vida_sexual, 
            uso_anticonceptivos, numero_embarazos, numero_partos, numero_cesareas, observaciones
        FROM antecedentes_ginecobstetricos
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchone()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/consultarPadecimientoActual', methods=['POST'])
def consultar_padecimiento_actual():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT descripcion
        FROM antecedentes_padecimientoactual
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchone()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/consultarExploracion', methods=['POST'])
def consultar_exploracion():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            habitus_exterior, peso, altura, imc, temperatura, pulso_cardiaco, frecuencia_respiratoria, 
            presion_arterial, saturacion_oxigeno, observaciones, resultados_previos_actuales
        FROM exploracion
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchone()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/consultar_notas', methods=['POST'])
def consultar_notas():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)

        # Consulta a la tabla notas_seguimientos
        query = """
        SELECT id_ficha, nombre, diagnostico, folio, fecha, numero_sesion, notas, sugerencias_observaciones, nombreYfirma_tratante
        FROM notas_seguimientos
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        resultados = cursor.fetchall()

        if resultados:
            return jsonify({"datos": resultados})
        else:
            return jsonify({"error": "No se encontraron registros para el ID proporcionado"}), 404

    except mysql.connector.Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/consultar_plan_tratamiento', methods=['POST'])
def consultar_plan_tratamiento():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)

        # Consulta a la tabla plan_tratamientos
        query = """
        SELECT id_ficha, objetivo, modalidad_terapeutica AS modalidad, descripcion, dosis
        FROM plan_tratamientos
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        resultados = cursor.fetchall()

        if resultados:
            return jsonify({"datos": resultados})
        else:
            return jsonify({"error": "No se encontraron registros para el ID proporcionado"}), 404

    except mysql.connector.Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/consultarMiembrosSuperiores', methods=['POST'])
def consultar_miembros_superiores():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            observacion AS observacionesMiembrosSuperiores, 
            palpacion AS palpacionMiembrosSuperiores, 
            descripcion AS dolorSuperiorMiembrosSuperiores, 
            dolor AS dolorexplofisicaMiembrosSuperiores
        FROM partes_cuerpo_miembro_superior
        WHERE id_ficha = %s AND id_partes = 1
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchone()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/consultarFuerzaMuscularMiembrosSuperiores', methods=['POST'])
def consultar_fuerza_muscular_miembros_superiores():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            movimiento, izquierda AS izquierdo, derecha AS derecho
        FROM fuerza_muscular_miembro_superior
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchall()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarGoniometriaMiembrosSuperiores', methods=['POST'])
def consultar_goniometria_miembros_superiores():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            rango_normal AS rango, 
            movimiento, 
            izquierdo, 
            derecho
        FROM goniometria_miembro_superior
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchall()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarReflejosOsteotendinosos', methods=['POST'])
def consultar_reflejos_osteotendinosos():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            rot AS reflejo, 
            izq AS izquierdo, 
            der AS derecho
        FROM reflejososteotendinosos_miembro_superior
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchall()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarPruebasEvaluacionesComplementarias', methods=['POST'])
def consultar_pruebas_evaluaciones_complementarias():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            pruebas AS prueba, 
            resultadosyanalisis AS resultado
        FROM pruebasevaluacionescomplementarias_miembro_superior
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchall()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarMiembrosInferiores', methods=['POST'])
def consultar_miembros_inferiores():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            observacion AS observacionesMiembrosInferiores, 
            palpacion AS palpacionMiembrosInferiores, 
            descripcion AS dolorSuperiorMiembrosInferiores, 
            dolor AS dolorexplofisicaMiembrosInferiores
        FROM partes_cuerpo_miembro_inferior
        WHERE id_ficha = %s AND id_partes = 2
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchone()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarFuerzaMuscularMiembrosInferiores', methods=['POST'])
def consultar_fuerza_muscular_miembros_inferiores():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            movimiento, 
            izquierda, 
            derecha
        FROM fuerza_muscular_miembro_inferior
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchall()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/consultarGoniometriaMiembrosInferiores', methods=['POST'])
def consultar_goniometria_miembros_inferiores():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            rango_normal AS rango, 
            movimiento, 
            izquierdo, 
            derecho
        FROM goniometria_miembro_inferior
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchall()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarReflejosOsteotendinososMiembrosInferiores', methods=['POST'])
def consultar_reflejos_osteotendinosos_miembros_inferiores():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            rot AS reflejo, 
            izq AS izquierdo, 
            der AS derecho
        FROM reflejososteotendinosos_miembro_inferior
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchall()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarPruebasEvaluacionesComplementariasInferiores', methods=['POST'])
def consultar_pruebas_evaluaciones_complementarias_inferiores():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            pruebas AS prueba, 
            resultadosyanalisis AS resultado
        FROM pruebasevaluacionescomplementarias_miembro_inferior
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchall()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarCicloMarchaMiembrosInferiores', methods=['POST'])
def consultar_ciclo_marcha_miembros_inferiores():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            fase_apoyo_completo AS faseApoyoCompleto,
            contacto_talon_izquierdo AS contactoTalonIzquierdo,
            contacto_talon_derecho AS contactoTalonDerecho,
            apoyo_plantar_izquierdo AS apoyoPlantarIzquierdo,
            apoyo_plantar_derecho AS apoyoPlantarDerecho,
            apoyo_medio_izquierdo AS apoyoMedioIzquierdo,
            apoyo_medio_derecho AS apoyoMedioDerecho,
            fase_oscilacion_completo AS faseOscilacionCompleto,
            balanceo_inicial_izquierdo AS balanceoInicialIzquierdo,
            balanceo_inicial_derecho AS balanceoInicialDerecho,
            balanceo_medio_izquierdo AS balanceoMedioIzquierdo,
            balanceo_medio_derecho AS balanceoMedioDerecho,
            balanceo_terminal_izquierdo AS balanceoTerminalIzquierdo,
            balanceo_terminal_derecho AS balanceoTerminalDerecho,
            rotacion_pelvica_completo AS rotacionPelvicaCompleto,
            inclinacion_pelvica_completo AS inclinacionPelvicaCompleto,
            flexion_rodilla_izquierdo AS flexionRodillaIzquierdo,
            flexion_rodilla_derecho AS flexionRodillaDerecho,
            movimientos_coordinados_rodilla_tobillo_izquierdo AS movimientosCoordinadosRodillaTobilloIzquierdo,
            movimientos_coordinados_rodilla_tobillo_derecho AS movimientosCoordinadosRodillaTobilloDerecho,
            movimiento_centro_gravedad_completo AS movimientoCentroGravedadCompleto,
            cadencia_completo AS cadenciaCompleto,
            balanceo_ms_completo AS balanceoMSCompleto
        FROM ciclo_marcha_miembro_inferior
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchone()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarCabezaCuello', methods=['POST'])
def consultar_cabeza_cuello():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            observacion AS observacionesCabezaCuello, 
            palpacion AS palpacionCabezaCuello, 
            descripcion AS dolorSuperiorCabezaCuello, 
            dolor AS dolorexplofisicaCabezaCuello
        FROM partes_cuerpo_cabeza_y_torax
        WHERE id_ficha = %s AND id_partes = 3
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchone()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarFuerzaMuscularCabezaTorax', methods=['POST'])
def consultar_fuerza_muscular_cabeza_torax():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            movimiento, 
            valores_obtenidos AS valoresObtenidos
        FROM fuerza_muscular_cabeza_y_torax
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchall()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarColumnaToraxAbdomen', methods=['POST'])
def consultar_columna_torax_abdomen():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            observacion AS observacionesColumnaTóraxAbdomen, 
            palpacion AS palpacionColumnaTóraxAbdomen, 
            descripcion AS dolorSuperiorColumnaTóraxAbdomen, 
            dolor AS dolorexplofisicaColumnaTóraxAbdomen
        FROM partes_cuerpo_cabeza_y_torax1
        WHERE id_ficha = %s AND id_partes = 4
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchone()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarFuerzaMuscularCabezaTorax2', methods=['POST'])
def consultar_fuerza_muscular_cabeza_torax2():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            movimiento, 
            valores_obtenidos AS valoresObtenidos
        FROM fuerza_muscular_cabeza_y_torax1
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchall()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarGoniometriaCabezaTorax', methods=['POST'])
def consultar_goniometria_cabeza_torax():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            rangos_normales AS rango, 
            movimientos AS movimiento, 
            resultados
        FROM goniometria_cabeza_y_torax
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchall()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarPruebasEvaluacionesComplementariasCabezaTorax', methods=['POST'])
def consultar_pruebas_evaluaciones_complementarias_cabeza_torax():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            pruebas AS prueba, 
            resultadosyanalisis AS resultado
        FROM pruebasevaluacionescomplementarias_cabeza_y_torax
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchall()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarVistaFrontal', methods=['POST'])
def consultar_vista_frontal():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            alineacion_corporal AS alineacionCorporal, 
            observaciones AS ObservacionesvistaFrontal
        FROM vistafrontal
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchall()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarVistaLateral', methods=['POST'])
def consultar_vista_lateral():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            alineacion_corporal AS alineacionCorporal1, 
            observaciones AS ObservacionesvistaLateral
        FROM vistalateral
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchall()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
@app.route('/consultarVistaPosterior', methods=['POST'])
def consultar_vista_posterior():
    data = request.get_json()
    id_recibido = data.get('id')

    if not id_recibido:
        return jsonify({"error": "ID no proporcionado"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Error al conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT 
            alineacion_corporal AS alineacionCorporal2, 
            observaciones AS ObservacionesvistaPosterior
        FROM vistaposterior
        WHERE id_ficha = %s
        """
        cursor.execute(query, (id_recibido,))
        result = cursor.fetchall()

        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "No se encontraron datos para el ID proporcionado"}), 404

    except Error as e:
        return jsonify({"error": f"Error al realizar la consulta: {e}"}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()         
            
            
            
            
            
            
            


            
            
            












































































            
            
            
 
 
 
 
 
 
            
            
            
            
            
            
            
            
            
            
            
            
            


















    
@app.route('/EdicionRegistro')
def EdicionRegistro():
    return render_template('EdicionRegistro.html', current_page='EdicionRegistro')

@app.route('/EdicionFicha')
def EdicionFicha():
    return render_template('EdicionFicha.html', current_page='EdicionFicha')

@app.route('/EdicionNotasSeguimiento')
def EdicionNotasSeguimiento():
    return render_template('EdicionNotasSeguimiento.html', current_page='EdicionNotasSeguimiento')

@app.route('/EdicionPlanDiagnostico')
def EdicionPlanDiagnostico():
    return render_template('EdicionPlanDiagnostico.html', current_page='EdicionPlanDiagnostico')

@app.route('/EdicionMiembroSuperior')
def EdicionMiembroSuperior():
    return render_template('EdicionMiembroSuperior.html', current_page='EdicionMiembroSuperior')

@app.route('/EdicionMiembroInferior')
def EdicionMiembroInferior():
    return render_template('EdicionMiembroInferior.html', current_page='EdicionMiembroInferior')

@app.route('/EdicionCabezaTorax')
def EdicionCabezaTorax():
    return render_template('EdicionCabezaTorax.html', current_page='EdicionCabezaTorax')

@app.route('/EdicionEvaluacionDeLaPostura')
def EdicionEvaluacionDeLaPostura():
    return render_template('EdicionEvaluacionDeLaPostura.html', current_page='EdicionEvaluacionDeLaPostura')
            
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
        aleatorio = random.randint(1000, 9999)

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

@app.route('/actualizar_datos', methods=['PUT'])
def actualizar_datos():
    data = request.get_json()
    id_ficha1 = data.get('id')  # ID proporcionado desde el frontend

    if not id_ficha1:
        return jsonify({'success': False, 'error': 'ID no proporcionado'}), 400

    try:
        connection = create_connection()
        cursor = connection.cursor()

        # Actualización en la tabla ficha_identificaciones
        actualizar_ficha_identificaciones = """
        UPDATE ficha_identificaciones SET
            fecha_elaboracion = %s, folio = %s, nombre_paciente = %s, genero = %s, 
            fecha_nacimiento = %s, edad = %s, lugar_nacimiento = %s, estado_civil = %s, 
            ocupacion = %s, nacionalidad = %s, domicilio_actual = %s, telefono = %s, 
            contacto_emergencia_nombre = %s, contacto_emergencia_telefono = %s, 
            diagnostico_medico = %s, elaboro_historial_clinico = %s, motivo_consulta = %s
        WHERE id = %s
        """
        cursor.execute(actualizar_ficha_identificaciones, (
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
            data.get('motivoConsulta'),
            id_ficha1
        ))

        # Actualización en la tabla antecedentespersonalesnopatologicos
        actualizar_antecedentes_no_patologicos = """
        UPDATE antecedentespersonalesnopatologicos SET
            PropiaRenta = %s, Ventilacion = %s, Iluminacion = %s, Piso = %s, 
            Electrodomesticos = %s, Servicios = %s, DescripcionVivienda = %s, 
            NoComidasDia = %s, AguaLts = %s, GruposAlimenticios = %s, 
            DescripcionRutinaAlimenticia = %s, HigieneBucal = %s, BanosDia = %s, 
            CambiosRopa = %s, ActividadFisica = %s, Deporte = %s, Ocio = %s, Ocupacion = %s
        WHERE id_ficha = %s
        """
        cursor.execute(actualizar_antecedentes_no_patologicos, (
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
            data.get('Ocupacion1'),
            id_ficha1
        ))

        # Actualizar antecedentesheredofamiliares (ejemplo para listas)
        cursor.execute("DELETE FROM antecedentesheredofamiliares WHERE id_ficha = %s", (id_ficha1,))
        for antecedente in data.get('antecedentes', []):
            cursor.execute("""
            INSERT INTO antecedentesheredofamiliares (
                id_ficha, enfermedad, si, no, parentesco, vivo, muerto, otro, observaciones
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                id_ficha1,
                antecedente.get('enfermedad'),
                antecedente.get('si'),
                antecedente.get('no'),
                antecedente.get('parentesco'),
                antecedente.get('vivo'),
                antecedente.get('muerto'),
                antecedente.get('otro'),
                antecedente.get('observaciones')
            ))

        # Actualización en la tabla antecedentes_patologicos
        cursor.execute("DELETE FROM antecedentes_patologicos WHERE id_ficha = %s", (id_ficha1,))
        for patologia in data.get('datosPatologicos', []):
            insertar_antecedentes_patologicos = """
            INSERT INTO antecedentes_patologicos (
                id_ficha, patologia, si, no, edad_presentacion, secuelas_complicaciones, inmunizaciones, observaciones
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insertar_antecedentes_patologicos, (
                id_ficha1,
                patologia.get('patologia'),
                patologia.get('si_pa'),
                patologia.get('no_pa'),
                patologia.get('edad_presento'),
                patologia.get('secuela'),
                patologia.get('inmunizaciones'),
                patologia.get('observaciones1')
            ))

        # Actualización en la tabla antecedentes_ginecobstetricos
        actualizar_ginecobstetricos = """
        UPDATE antecedentes_ginecobstetricos SET
            menarquia = %s, fecha_ultima_menstruacion = %s, caracteristicas_menstruacion = %s, 
            inicio_vida_sexual = %s, uso_anticonceptivos = %s, numero_embarazos = %s, 
            numero_partos = %s, numero_cesareas = %s, observaciones = %s
        WHERE id_ficha = %s
        """
        cursor.execute(actualizar_ginecobstetricos, (
            data.get('menarquia'),
            data.get('fecha_ultima_menstruacion'),
            data.get('caracteristicas_menstruacion'),
            data.get('inicio_vida_sexual'),
            data.get('uso_anticonceptivos'),
            data.get('numero_embarazos'),
            data.get('numero_partos'),
            data.get('numero_cesareas'),
            data.get('observaciones_gine'),
            id_ficha1
        ))

        # Actualización en la tabla antecedentes_padecimientoactual
        actualizar_padecimientoactual = """
        UPDATE antecedentes_padecimientoactual SET
            descripcion = %s
        WHERE id_ficha = %s
        """
        cursor.execute(actualizar_padecimientoactual, (
            data.get('ac_descripcion'),
            id_ficha1
        ))

        # Actualización en la tabla exploracion
        actualizar_exploracion = """
        UPDATE exploracion SET
            habitus_exterior = %s, peso = %s, altura = %s, imc = %s, 
            temperatura = %s, pulso_cardiaco = %s, frecuencia_respiratoria = %s, 
            presion_arterial = %s, saturacion_oxigeno = %s, observaciones = %s, 
            resultados_previos_actuales = %s
        WHERE id_ficha = %s
        """
        cursor.execute(actualizar_exploracion, (
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
            data.get('resultados_previos_actuales'),
            id_ficha1
        ))
# -------------------------------------------------------------------------------------------------------------------------------------------------------

        # Actualización en la tabla partes_cuerpo_miembro_superior
        actualizar_miembro_superior = """
        UPDATE partes_cuerpo_miembro_superior SET
            id_partes = %s, observacion = %s, palpacion = %s, descripcion = %s, dolor = %s
        WHERE id_ficha = %s
        """
        cursor.execute(actualizar_miembro_superior, (
            1,
            data.get('observacionesMiembrosSuperiores'),
            data.get('palpacionMiembrosSuperiores'),
            data.get('dolorSuperiorMiembrosSuperiores'),
            data.get('dolorexplofisicaMiembrosSuperiores'),
            id_ficha1
        ))

        # Actualización en la tabla fuerza_muscular_miembro_superior
        cursor.execute("DELETE FROM fuerza_muscular_miembro_superior WHERE id_ficha = %s", (id_ficha1,))
        for movimiento in data.get('fuerzaMuscularMiembrosSuperiores', []):
            insertar_fuerza_muscular = """
            INSERT INTO fuerza_muscular_miembro_superior (
                id_ficha, derecha, movimiento, izquierda
            ) VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insertar_fuerza_muscular, (
                id_ficha1,
                movimiento.get('derecho'),
                movimiento.get('movimiento'),
                movimiento.get('izquierdo')
            ))

        # Actualización en la tabla goniometria_miembro_superior
        cursor.execute("DELETE FROM goniometria_miembro_superior WHERE id_ficha = %s", (id_ficha1,))
        for goniometria in data.get('goniometriaMiembrosSuperiores', []):
            insertar_goniometria = """
            INSERT INTO goniometria_miembro_superior (
                id_ficha, rango_normal, izquierdo, movimiento, derecho
            ) VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insertar_goniometria, (
                id_ficha1,
                goniometria.get('rango'),
                goniometria.get('izquierdo'),
                goniometria.get('movimiento'),
                goniometria.get('derecho')
            ))

        # Actualización en la tabla reflejososteotendinosos_miembro_superior
        cursor.execute("DELETE FROM reflejososteotendinosos_miembro_superior WHERE id_ficha = %s", (id_ficha1,))
        for reflejo in data.get('reflejosOsteotendinososMiembrosSuperiores', []):
            insertar_reflejo = """
            INSERT INTO reflejososteotendinosos_miembro_superior (
                id_ficha, izq, rot, der
            ) VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insertar_reflejo, (
                id_ficha1,
                reflejo.get('izquierdo'),
                reflejo.get('reflejo'),
                reflejo.get('derecho')
            ))

        # Actualización en la tabla pruebas_evaluaciones_complementarias_miembro_superior
        cursor.execute("DELETE FROM pruebasevaluacionescomplementarias_miembro_superior WHERE id_ficha = %s", (id_ficha1,))
        for prueba in data.get('pruebasEvaluacionesComplementariasMiembrosSuperiores', []):
            insertar_pruebas = """
            INSERT INTO pruebasevaluacionescomplementarias_miembro_superior (
                id_ficha, pruebas, resultadosyanalisis
            ) VALUES (%s, %s, %s)
            """
            cursor.execute(insertar_pruebas, (
                id_ficha1,
                prueba.get('prueba'),
                prueba.get('resultado')
            ))

# -------------------------------------------------------------------------------------------------------------------------------------------------------

            # Actualización en la tabla partes_cuerpo_miembro_inferior
            actualizar_miembro_inferior = """
            UPDATE partes_cuerpo_miembro_inferior SET
                id_partes = %s, observacion = %s, palpacion = %s, descripcion = %s, dolor = %s
            WHERE id_ficha = %s
            """
            cursor.execute(actualizar_miembro_inferior, (
                2,
                data.get('observacionesMiembrosInferiores'),
                data.get('palpacionMiembrosInferiores'),
                data.get('dolorSuperiorMiembrosInferiores'),
                data.get('dolorexplofisicaMiembrosInferiores'),
                id_ficha1
            ))

            # Actualización en la tabla fuerza_muscular_miembro_inferior
            cursor.execute("DELETE FROM fuerza_muscular_miembro_inferior WHERE id_ficha = %s", (id_ficha1,))
            for movimiento in data.get('fuerzaMuscularMiembrosInferiores', []):
                insertar_fuerza_muscular = """
                INSERT INTO fuerza_muscular_miembro_inferior (
                    id_ficha, derecha, movimiento, izquierda
                ) VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insertar_fuerza_muscular, (
                    id_ficha1,
                    movimiento['derecho'],
                    movimiento['movimiento'],
                    movimiento['izquierdo']
                ))

            # Actualización en la tabla goniometria_miembro_inferior
            cursor.execute("DELETE FROM goniometria_miembro_inferior WHERE id_ficha = %s", (id_ficha1,))
            for goniometria in data.get('goniometriaMiembrosInferiores', []):
                insertar_goniometria = """
                INSERT INTO goniometria_miembro_inferior (
                    id_ficha, rango_normal, izquierdo, movimiento, derecho
                ) VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(insertar_goniometria, (
                    id_ficha1,
                    goniometria.get('rango'),
                    goniometria.get('izquierdo'),
                    goniometria.get('movimiento'),
                    goniometria.get('derecho')
                ))

            # Actualización en la tabla reflejososteotendinosos_miembro_inferior
            cursor.execute("DELETE FROM reflejososteotendinosos_miembro_inferior WHERE id_ficha = %s", (id_ficha1,))
            for reflejo in data.get('reflejosOsteotendinososMiembrosInferiores', []):
                insertar_reflejo = """
                INSERT INTO reflejososteotendinosos_miembro_inferior (
                    id_ficha, izq, rot, der
                ) VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insertar_reflejo, (
                    id_ficha1,
                    reflejo['izquierdo'],
                    reflejo['reflejo'],
                    reflejo['derecho']
                ))

            # Actualización en la tabla pruebasevaluacionescomplementarias_miembro_inferior
            cursor.execute("DELETE FROM pruebasevaluacionescomplementarias_miembro_inferior WHERE id_ficha = %s", (id_ficha1,))
            for prueba in data.get('pruebasEvaluacionesComplementariasMiembrosInferiores', []):
                insertar_pruebas = """
                INSERT INTO pruebasevaluacionescomplementarias_miembro_inferior (
                    id_ficha, pruebas, resultadosyanalisis
                ) VALUES (%s, %s, %s)
                """
                cursor.execute(insertar_pruebas, (
                    id_ficha1,
                    prueba.get('prueba'),
                    prueba.get('resultado')
                ))

            # Actualización en la tabla ciclo_marcha_miembro_inferior
            evaluacion_marcha = data.get('evaluacionMarcha', {})
            actualizar_ciclo_marcha = """
            UPDATE ciclo_marcha_miembro_inferior SET
                fase_apoyo_completo = %s, contacto_talon_izquierdo = %s, contacto_talon_derecho = %s, 
                apoyo_plantar_izquierdo = %s, apoyo_plantar_derecho = %s, apoyo_medio_izquierdo = %s, 
                apoyo_medio_derecho = %s, fase_oscilacion_completo = %s, balanceo_inicial_izquierdo = %s, 
                balanceo_inicial_derecho = %s, balanceo_medio_izquierdo = %s, balanceo_medio_derecho = %s, 
                balanceo_terminal_izquierdo = %s, balanceo_terminal_derecho = %s, rotacion_pelvica_completo = %s, 
                inclinacion_pelvica_completo = %s, flexion_rodilla_izquierdo = %s, flexion_rodilla_derecho = %s, 
                movimientos_coordinados_rodilla_tobillo_izquierdo = %s, movimientos_coordinados_rodilla_tobillo_derecho = %s, 
                movimiento_centro_gravedad_completo = %s, cadencia_completo = %s, balanceo_ms_completo = %s
            WHERE id_ficha = %s
            """
            cursor.execute(actualizar_ciclo_marcha, (
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
                evaluacion_marcha.get('balanceoMSCompleto'),
                id_ficha1
            ))

# -------------------------------------------------------------------------------------------------------------------------------------------------------

            # Actualización en la tabla partes_cuerpo_cabeza_y_torax
            actualizar_partes_cuerpo_cabeza_y_torax = """
            UPDATE partes_cuerpo_cabeza_y_torax SET
                id_partes = %s, observacion = %s, palpacion = %s, descripcion = %s, dolor = %s
            WHERE id_ficha = %s
            """
            cursor.execute(actualizar_partes_cuerpo_cabeza_y_torax, (
                3,  # Valor fijo para `id_partes`
                data.get('observacionesCabezaCuello'),
                data.get('palpacionCabezaCuello'),
                data.get('dolorSuperiorCabezaCuello'),
                data.get('dolorexplofisicaCabezaCuello'),
                id_ficha1
            ))

            # Actualización en la tabla fuerza_muscular_cabeza_y_torax
            cursor.execute("DELETE FROM fuerza_muscular_cabeza_y_torax WHERE id_ficha = %s", (id_ficha1,))
            for movimiento in data.get('fuerzaMuscularCabezaTorax1', []):
                insertar_fuerza_muscular_cabeza_y_torax = """
                INSERT INTO fuerza_muscular_cabeza_y_torax (
                    id_ficha, movimiento, valores_obtenidos
                ) VALUES (%s, %s, %s)
                """
                cursor.execute(insertar_fuerza_muscular_cabeza_y_torax, (
                    id_ficha1,
                    movimiento['movimiento'],
                    movimiento['valoresObtenidos']
                ))

            # Actualización en la tabla partes_cuerpo_cabeza_y_torax1
            actualizar_partes_cuerpo_cabeza_y_torax1 = """
            UPDATE partes_cuerpo_cabeza_y_torax1 SET
                id_partes = %s, observacion = %s, palpacion = %s, descripcion = %s, dolor = %s
            WHERE id_ficha = %s
            """
            cursor.execute(actualizar_partes_cuerpo_cabeza_y_torax1, (
                4,  # Valor fijo para `id_partes`
                data.get('observacionesColumnaTóraxAbdomen'),
                data.get('palpacionColumnaTóraxAbdomen'),
                data.get('dolorSuperiorColumnaTóraxAbdomen'),
                data.get('dolorexplofisicaColumnaTóraxAbdomen'),
                id_ficha1
            ))

            # Actualización en la tabla fuerza_muscular_cabeza_y_torax1
            cursor.execute("DELETE FROM fuerza_muscular_cabeza_y_torax1 WHERE id_ficha = %s", (id_ficha1,))
            for movimiento in data.get('fuerzaMuscularCabezaTorax2', []):
                insertar_fuerza_muscular_cabeza_y_torax1 = """
                INSERT INTO fuerza_muscular_cabeza_y_torax1 (
                    id_ficha, movimiento, valores_obtenidos
                ) VALUES (%s, %s, %s)
                """
                cursor.execute(insertar_fuerza_muscular_cabeza_y_torax1, (
                    id_ficha1,
                    movimiento['movimiento'],
                    movimiento['valoresObtenidos']
                ))

            # Actualización en la tabla goniometria_cabeza_y_torax
            cursor.execute("DELETE FROM goniometria_cabeza_y_torax WHERE id_ficha = %s", (id_ficha1,))
            for goniometria in data.get('goniometriaCabezaTorax', []):
                insertar_goniometria_cabeza_y_torax = """
                INSERT INTO goniometria_cabeza_y_torax (
                    id_ficha, rangos_normales, movimientos, resultados
                ) VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insertar_goniometria_cabeza_y_torax, (
                    id_ficha1,
                    goniometria['rango'],
                    goniometria['movimiento'],
                    goniometria['resultados']
                ))

            # Actualización en la tabla pruebas_evaluaciones_complementarias_cabeza_y_torax
            cursor.execute("DELETE FROM pruebasevaluacionescomplementarias_cabeza_y_torax WHERE id_ficha = %s", (id_ficha1,))
            for prueba in data.get('pruebasEvaluacionesComplementariasCabezaTorax', []):
                insertar_pruebas_evaluaciones_complementarias_cabeza_y_torax = """
                INSERT INTO pruebasevaluacionescomplementarias_cabeza_y_torax (
                    id_ficha, pruebas, resultadosyanalisis
                ) VALUES (%s, %s, %s)
                """
                cursor.execute(insertar_pruebas_evaluaciones_complementarias_cabeza_y_torax, (
                    id_ficha1,
                    prueba['prueba'],
                    prueba['resultado']
                ))

# -------------------------------------------------------------------------------------------------------------------------------------------------------

            # Actualización en la tabla vistafrontal
            cursor.execute("DELETE FROM vistafrontal WHERE id_ficha = %s", (id_ficha1,))
            for vista in data.get('vistaFrontal', []):
                insertar_vista_frontal = """
                INSERT INTO vistafrontal (id_ficha, alineacion_corporal, observaciones)
                VALUES (%s, %s, %s)
                """
                cursor.execute(insertar_vista_frontal, (
                    id_ficha1,
                    vista.get('alineacionCorporal'),
                    vista.get('ObservacionesvistaFrontal')
                ))

            # Actualización en la tabla vistalateral
            cursor.execute("DELETE FROM vistalateral WHERE id_ficha = %s", (id_ficha1,))
            for vista in data.get('vistaLateral', []):
                insertar_vista_lateral = """
                INSERT INTO vistalateral (id_ficha, alineacion_corporal, observaciones)
                VALUES (%s, %s, %s)
                """
                cursor.execute(insertar_vista_lateral, (
                    id_ficha1,
                    vista.get('alineacionCorporal1'),
                    vista.get('ObservacionesvistaLateral')
                ))

            # Actualización en la tabla vistaposterior
            cursor.execute("DELETE FROM vistaposterior WHERE id_ficha = %s", (id_ficha1,))
            for vista in data.get('vistaPosterior', []):
                insertar_vista_posterior = """
                INSERT INTO vistaposterior (id_ficha, alineacion_corporal, observaciones)
                VALUES (%s, %s, %s)
                """
                cursor.execute(insertar_vista_posterior, (
                    id_ficha1,
                    vista.get('alineacionCorporal2'),
                    vista.get('ObservacionesvistaPosterior')
                ))

# -------------------------------------------------------------------------------------------------------------------------------------------------------

            # Eliminar los datos existentes en la tabla notas_seguimientos
            cursor.execute("DELETE FROM notas_seguimientos WHERE id_ficha = %s", (id_ficha1,))

            # Insertar el dato principal en la tabla notas_seguimientos
            datosPrincipal = data.get('principal', {})
            sql = """
            INSERT INTO notas_seguimientos (
                id_ficha, nombre, diagnostico, folio, fecha, numero_sesion, notas, sugerencias_observaciones, nombreYfirma_tratante
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                id_ficha1,
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

            # Insertar cada sección adicional en la tabla notas_seguimientos
            for seccion in data.get('secciones', []):
                valores_seccion = (
                    id_ficha1,
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

# -------------------------------------------------------------------------------------------------------------------------------------------------------

            # Eliminar los datos existentes en la tabla plan_tratamientos
            cursor.execute("DELETE FROM plan_tratamientos WHERE id_ficha = %s", (id_ficha1,))

            # Insertar los datos actualizados en la tabla plan_tratamientos
            plan_tratamiento = data.get('planTratamiento', [])
            for tratamiento in plan_tratamiento:
                insertar_plan_tratamiento = """
                INSERT INTO plan_tratamientos (
                    id_ficha, objetivo, modalidad_terapeutica, descripcion, dosis
                ) VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(insertar_plan_tratamiento, (
                    id_ficha1,
                    tratamiento.get('objetivo'),
                    tratamiento.get('modalidad'),
                    tratamiento.get('descripcion'),
                    tratamiento.get('dosis')
                ))

        connection.commit()
        return jsonify({'success': True})
    except Error as e:
        print(f"Error al actualizar en la base de datos: {e}")
        return jsonify({'success': False, 'error': str(e)})
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

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
            
# -------------------------------------------------------------------------------------------------------------------------------------------------------            

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
            
# -------------------------------------------------------------------------------------------------------------------------------------------------------            

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
        # Consulta original para ficha_identificaciones
        "SELECT * FROM ficha_identificaciones",

        # Consultas adaptadas para incluir nombre_paciente al principio
        "SELECT ficha_identificaciones.nombre_paciente, antecedentespersonalesnopatologicos.* FROM antecedentespersonalesnopatologicos JOIN ficha_identificaciones ON antecedentespersonalesnopatologicos.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, antecedentesheredofamiliares.* FROM antecedentesheredofamiliares JOIN ficha_identificaciones ON antecedentesheredofamiliares.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, antecedentes_patologicos.* FROM antecedentes_patologicos JOIN ficha_identificaciones ON antecedentes_patologicos.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, antecedentes_ginecobstetricos.* FROM antecedentes_ginecobstetricos JOIN ficha_identificaciones ON antecedentes_ginecobstetricos.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, antecedentes_padecimientoactual.* FROM antecedentes_padecimientoactual JOIN ficha_identificaciones ON antecedentes_padecimientoactual.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, exploracion.* FROM exploracion JOIN ficha_identificaciones ON exploracion.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, partes_cuerpo_miembro_superior.* FROM partes_cuerpo_miembro_superior JOIN ficha_identificaciones ON partes_cuerpo_miembro_superior.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, fuerza_muscular_miembro_superior.* FROM fuerza_muscular_miembro_superior JOIN ficha_identificaciones ON fuerza_muscular_miembro_superior.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, goniometria_miembro_superior.* FROM goniometria_miembro_superior JOIN ficha_identificaciones ON goniometria_miembro_superior.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, reflejososteotendinosos_miembro_superior.* FROM reflejososteotendinosos_miembro_superior JOIN ficha_identificaciones ON reflejososteotendinosos_miembro_superior.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, pruebasevaluacionescomplementarias_miembro_superior.* FROM pruebasevaluacionescomplementarias_miembro_superior JOIN ficha_identificaciones ON pruebasevaluacionescomplementarias_miembro_superior.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, partes_cuerpo_miembro_inferior.* FROM partes_cuerpo_miembro_inferior JOIN ficha_identificaciones ON partes_cuerpo_miembro_inferior.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, fuerza_muscular_miembro_inferior.* FROM fuerza_muscular_miembro_inferior JOIN ficha_identificaciones ON fuerza_muscular_miembro_inferior.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, goniometria_miembro_inferior.* FROM goniometria_miembro_inferior JOIN ficha_identificaciones ON goniometria_miembro_inferior.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, reflejososteotendinosos_miembro_inferior.* FROM reflejososteotendinosos_miembro_inferior JOIN ficha_identificaciones ON reflejososteotendinosos_miembro_inferior.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, pruebasevaluacionescomplementarias_miembro_inferior.* FROM pruebasevaluacionescomplementarias_miembro_inferior JOIN ficha_identificaciones ON pruebasevaluacionescomplementarias_miembro_inferior.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, ciclo_marcha_miembro_inferior.* FROM ciclo_marcha_miembro_inferior JOIN ficha_identificaciones ON ciclo_marcha_miembro_inferior.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, partes_cuerpo_cabeza_y_torax.* FROM partes_cuerpo_cabeza_y_torax JOIN ficha_identificaciones ON partes_cuerpo_cabeza_y_torax.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, fuerza_muscular_cabeza_y_torax.* FROM fuerza_muscular_cabeza_y_torax JOIN ficha_identificaciones ON fuerza_muscular_cabeza_y_torax.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, partes_cuerpo_cabeza_y_torax1.* FROM partes_cuerpo_cabeza_y_torax1 JOIN ficha_identificaciones ON partes_cuerpo_cabeza_y_torax1.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, fuerza_muscular_cabeza_y_torax1.* FROM fuerza_muscular_cabeza_y_torax1 JOIN ficha_identificaciones ON fuerza_muscular_cabeza_y_torax1.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, goniometria_cabeza_y_torax.* FROM goniometria_cabeza_y_torax JOIN ficha_identificaciones ON goniometria_cabeza_y_torax.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, pruebasevaluacionescomplementarias_cabeza_y_torax.* FROM pruebasevaluacionescomplementarias_cabeza_y_torax JOIN ficha_identificaciones ON pruebasevaluacionescomplementarias_cabeza_y_torax.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, vistafrontal.* FROM vistafrontal JOIN ficha_identificaciones ON vistafrontal.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, vistalateral.* FROM vistalateral JOIN ficha_identificaciones ON vistalateral.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, vistaposterior.* FROM vistaposterior JOIN ficha_identificaciones ON vistaposterior.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, plan_tratamientos.* FROM plan_tratamientos JOIN ficha_identificaciones ON plan_tratamientos.id_ficha = ficha_identificaciones.id",
        
        "SELECT ficha_identificaciones.nombre_paciente, notas_seguimientos.* FROM notas_seguimientos JOIN ficha_identificaciones ON notas_seguimientos.id_ficha = ficha_identificaciones.id"
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
