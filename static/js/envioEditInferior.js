// Función para obtener el valor de un campo de texto
const obtenerValor = id => document.getElementById(id)?.value || 'No hay información';
const obtenerValorNumerico = id => parseFloat(document.getElementById(id)?.value) || 0;
const obtenerValorEntero = id => parseInt(document.getElementById(id)?.value, 10) || 0;


function guardarDatosMiembroInferiores() {
    const datosMiembroInferiores = {
        // Miembros Inferiores
        observacionesMiembrosInferiores: obtenerValor('observacionesMiembrosInferiores'),
        palpacionMiembrosInferiores: obtenerValor('palpacionMiembrosInferiores'),
        dolorSuperiorMiembrosInferiores: obtenerValor('dolorSuperiorMiembrosInferiores'),
        dolorexplofisicaMiembrosInferiores: obtenerValorEntero('dolorexplofisicaMiembrosInferiores'),
        // Fuerza Muscular
        fuerzaMuscularMiembrosInferiores: ['Flexión de cadera', 'Extensión de la cadera', 'Abducción de la cadera', 'Aducción de la cadera',
            'Rotación externa de la cadera', 'Rotación interna de la cadera', 'Flexión de la rodilla', 'Extensión de la rodilla', 'Flexión plantar del tobillo',
            'Dorsiflexión e inversión del pie', 'Inversión del pie', 'Eversión del pie con flexión plantar', 'Eversión del pie con dorsiflexión'
        ].map(movimiento => ({
            movimiento,
            izquierdo: document.querySelector(`input[name="${movimiento}_izquierdo"]`)?.value || 'No hay información',
            derecho: document.querySelector(`input[name="${movimiento}_derecho"]`)?.value || 'No hay información',
        })),
        // Goniometría
        goniometriaMiembrosInferiores: [
            { rango: '0°-140°', movimiento: 'Flexión de cadera' }, { rango: '0°-10°', movimiento: 'Extensión de cadera' },
            { rango: '0°-50°', movimiento: 'Abducción de cadera' }, { rango: '0°-30°', movimiento: 'Aducción de cadera' },
            { rango: '0°-50°', movimiento: 'Rotación externa de cadera' }, { rango: '0°-40°', movimiento: 'Rotación interna de cadera' },
            { rango: '0°-150°', movimiento: 'Flexión de rodilla' }, { rango: '0°(activa)-10°(pasiva)', movimiento: 'Extensión de rodilla' },
            { rango: '0°-50°', movimiento: 'Plantiflexión' }, { rango: '0°-30°', movimiento: 'Dorsiflexión' },
            { rango: '0°-60°', movimiento: 'Inversión del pie' }, { rango: '0°-30°', movimiento: 'Eversión del pie' }
        ].map(rangoMovimiento => ({
            ...rangoMovimiento,
            izquierdo: document.querySelector(`input[name="${rangoMovimiento.rango}_${rangoMovimiento.movimiento}_izquierdo"]`)?.value || 'No hay información',
            derecho: document.querySelector(`input[name="${rangoMovimiento.rango}_${rangoMovimiento.movimiento}_derecho"]`)?.value || 'No hay información',
        })),
        // Reflejos Osteotendinosos
        reflejosOsteotendinososMiembrosInferiores: [
            'Rotuliano', 'Aquileo'
        ].map(reflejo => ({
            reflejo,
            izquierdo: document.querySelector(`input[name="${reflejo}_izq"]`)?.value || 'No hay información',
            derecho: document.querySelector(`input[name="${reflejo}_der"]`)?.value || 'No hay información',
        })),
        // Pruebas y Evaluaciones Complementarias
        pruebasEvaluacionesComplementariasMiembrosInferiores: [
            '1', '2', '3', '4'
        ].map((numero) => ({
            prueba: document.querySelector(`input[name="Pruebas_${numero}_MiembrosInferiores"]`)?.value || 'No hay información',
            resultado: document.querySelector(`input[name="Resultados y análisis_${numero}_MiembrosInferiores"]`)?.value || 'No hay información',
        })),
        // Evaluación de la marcha
        evaluacionMarcha: {
            faseApoyoCompleto: document.querySelector('input[name="Fase_de_apoyo_completo"]')?.value || 'No hay información',
            contactoTalonIzquierdo: document.querySelector('input[name="Contacto_de_talon_izquierdo"]')?.value || 'No hay información',
            contactoTalonDerecho: document.querySelector('input[name="Contacto_de_talon_derecho"]')?.value || 'No hay información',
            apoyoPlantarIzquierdo: document.querySelector('input[name="Apoyo_plantar_izquierdo"]')?.value || 'No hay información',
            apoyoPlantarDerecho: document.querySelector('input[name="Apoyo_plantar_derecho"]')?.value || 'No hay información',
            apoyoMedioIzquierdo: document.querySelector('input[name="Apoyo_medio_izquierdo"]')?.value || 'No hay información',
            apoyoMedioDerecho: document.querySelector('input[name="Apoyo_medio_derecho"]')?.value || 'No hay información',
            faseOscilacionCompleto: document.querySelector('input[name="Fase_de_oscilacion_completo"]')?.value || 'No hay información',
            balanceoInicialIzquierdo: document.querySelector('input[name="Balanceo_inicial_izquierdo"]')?.value || 'No hay información',
            balanceoInicialDerecho: document.querySelector('input[name="Balanceo_inicial_derecho"]')?.value || 'No hay información',
            balanceoMedioIzquierdo: document.querySelector('input[name="Balanceo_medio_izquierdo"]')?.value || 'No hay información',
            balanceoMedioDerecho: document.querySelector('input[name="Balanceo_medio_derecho"]')?.value || 'No hay información',
            balanceoTerminalIzquierdo: document.querySelector('input[name="Balanceo_terminal_izquierdo"]')?.value || 'No hay información',
            balanceoTerminalDerecho: document.querySelector('input[name="Balanceo_terminal_derecho"]')?.value || 'No hay información',
            rotacionPelvicaCompleto: document.querySelector('input[name="Rotacion_pelvica_completo"]')?.value || 'No hay información',
            inclinacionPelvicaCompleto: document.querySelector('input[name="Inclinacion_pelvica_completo"]')?.value || 'No hay información',
            flexionRodillaIzquierdo: document.querySelector('input[name="Flexion_de_rodilla_izquierdo"]')?.value || 'No hay información',
            flexionRodillaDerecho: document.querySelector('input[name="Flexion_de_rodilla_derecho"]')?.value || 'No hay información',
            movimientosCoordinadosRodillaTobilloIzquierdo: document.querySelector('input[name="Movimientos_coordinados_de_rodilla_y_tobillo_izquierdo"]')?.value || 'No hay información',
            movimientosCoordinadosRodillaTobilloDerecho: document.querySelector('input[name="Movimientos_coordinados_de_rodilla_y_tobillo_derecho"]')?.value || 'No hay información',
            movimientoCentroGravedadCompleto: document.querySelector('input[name="Movimiento_del_centro_de_gravedad_completo"]')?.value || 'No hay información',
            cadenciaCompleto: document.querySelector('input[name="Cadencia_completo"]')?.value || 'No hay información',
            balanceoMSCompleto: document.querySelector('input[name="Balanceo_de_MS_completo"]')?.value || 'No hay información'
        }
    };
    localStorage.setItem('datosMiembroInferiores', JSON.stringify(datosMiembroInferiores));
}



document.getElementById('miembroFormInferior').addEventListener('submit', function (event) {
    event.preventDefault();
    guardarDatosMiembroInferiores();
    window.location.href = '/EdicionCabezaTorax'; // Redirige a la página de resumen
});

document.querySelectorAll('input, select, textarea').forEach(element => {
    element.addEventListener('change', guardarDatosMiembroInferiores);
});

// Obtener los botones por su ID
const botonVisible = document.getElementById('botonVisible');
const botonOculto = document.getElementById('botonOculto');
// Agregar un evento de clic al botón visible
botonVisible.addEventListener('click', function () {
    // Disparar el evento de clic del botón oculto
    botonOculto.click();
});

// ---------------------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function () {

    // Función para guardar los datos del formulario 'miembroFormInferior' en localStorage
    function saveFormDataInferior() {
        const formData = {};
        const inputs = document.querySelectorAll("#miembroFormInferior input, #miembroFormInferior textarea");
        inputs.forEach(input => {
            formData[input.id] = input.value;
        });
        localStorage.setItem("miembroFormInferiorData", JSON.stringify(formData));
    }

    // Función para cargar los datos del formulario 'miembroFormInferior' desde localStorage
    function loadFormDataInferior() {
        const formData = JSON.parse(localStorage.getItem("miembroFormInferiorData"));
        if (formData) {
            const inputs = document.querySelectorAll("#miembroFormInferior input, #miembroFormInferior textarea");
            inputs.forEach(input => {
                if (formData[input.id]) {
                    input.value = formData[input.id];
                }
            });
        }
    }

    // Función para guardar los datos del formulario 'miembroFormInferior1' en localStorage
    function saveFormDataInferior1() {
        const formData1 = {};
        const inputs1 = document.querySelectorAll("#miembroFormInferior1 input");
        inputs1.forEach(input => {
            formData1[input.name] = input.value;
        });
        localStorage.setItem("miembroFormInferior1Data", JSON.stringify(formData1));
    }

    // Función para cargar los datos del formulario 'miembroFormInferior1' desde localStorage
    function loadFormDataInferior1() {
        const formData1 = JSON.parse(localStorage.getItem("miembroFormInferior1Data"));
        if (formData1) {
            const inputs1 = document.querySelectorAll("#miembroFormInferior1 input");
            inputs1.forEach(input => {
                if (formData1[input.name]) {
                    input.value = formData1[input.name];
                }
            });
        }
    }

    // Función para guardar los datos del formulario 'miembroFormInferior2' en localStorage
    function saveFormDataInferior2() {
        const formData2 = {};
        const inputs2 = document.querySelectorAll("#miembroFormInferior2 input");
        inputs2.forEach(input => {
            formData2[input.name] = input.value;
        });
        localStorage.setItem("miembroFormInferior2Data", JSON.stringify(formData2));
    }

    // Función para cargar los datos del formulario 'miembroFormInferior2' desde localStorage
    function loadFormDataInferior2() {
        const formData2 = JSON.parse(localStorage.getItem("miembroFormInferior2Data"));
        if (formData2) {
            const inputs2 = document.querySelectorAll("#miembroFormInferior2 input");
            inputs2.forEach(input => {
                if (formData2[input.name]) {
                    input.value = formData2[input.name];
                }
            });
        }
    }

    // Función para guardar los datos del formulario 'miembroFormInferior3' en localStorage
    function saveFormDataInferior3() {
        const formData3 = {};
        const inputs3 = document.querySelectorAll("#miembroFormInferior3 input");
        inputs3.forEach(input => {
            formData3[input.name] = input.value;
        });
        localStorage.setItem("miembroFormInferior3Data", JSON.stringify(formData3));
    }

    // Función para cargar los datos del formulario 'miembroFormInferior3' desde localStorage
    function loadFormDataInferior3() {
        const formData3 = JSON.parse(localStorage.getItem("miembroFormInferior3Data"));
        if (formData3) {
            const inputs3 = document.querySelectorAll("#miembroFormInferior3 input");
            inputs3.forEach(input => {
                if (formData3[input.name]) {
                    input.value = formData3[input.name];
                }
            });
        }
    }

    // Función para guardar los datos del formulario 'miembroFormInferior4' en localStorage
    function saveFormDataInferior4() {
        const formData4 = {};
        const inputs4 = document.querySelectorAll("#miembroFormInferior4 input");
        inputs4.forEach(input => {
            formData4[input.name] = input.value;
        });
        localStorage.setItem("miembroFormInferior4Data", JSON.stringify(formData4));
    }

    // Función para cargar los datos del formulario 'miembroFormInferior4' desde localStorage
    function loadFormDataInferior4() {
        const formData4 = JSON.parse(localStorage.getItem("miembroFormInferior4Data"));
        if (formData4) {
            const inputs4 = document.querySelectorAll("#miembroFormInferior4 input");
            inputs4.forEach(input => {
                if (formData4[input.name]) {
                    input.value = formData4[input.name];
                }
            });
        }
    }

    // Función para guardar los datos del formulario 'miembroFormInferior5' en localStorage
    function saveFormDataInferior5() {
        const formData5 = {};
        const inputs5 = document.querySelectorAll("#miembroFormInferior5 input");
        inputs5.forEach(input => {
            formData5[input.name] = input.value;
        });
        localStorage.setItem("miembroFormInferior5Data", JSON.stringify(formData5));
    }

    // Función para cargar los datos del formulario 'miembroFormInferior5' desde localStorage
    function loadFormDataInferior5() {
        const formData5 = JSON.parse(localStorage.getItem("miembroFormInferior5Data"));
        if (formData5) {
            const inputs5 = document.querySelectorAll("#miembroFormInferior5 input");
            inputs5.forEach(input => {
                if (formData5[input.name]) {
                    input.value = formData5[input.name];
                }
            });
        }
    }

    // Cargar datos al cargar la página
    loadFormDataInferior();
    loadFormDataInferior1();
    loadFormDataInferior2();
    loadFormDataInferior3();
    loadFormDataInferior4();
    loadFormDataInferior5();

    // Guardar datos en tiempo real para 'miembroFormInferior'
    const inputs = document.querySelectorAll("#miembroFormInferior input, #miembroFormInferior textarea");
    inputs.forEach(input => {
        input.addEventListener("input", saveFormDataInferior);
    });

    // Guardar datos en tiempo real para 'miembroFormInferior1'
    const inputs1 = document.querySelectorAll("#miembroFormInferior1 input");
    inputs1.forEach(input => {
        input.addEventListener("input", saveFormDataInferior1);
    });

    // Guardar datos en tiempo real para 'miembroFormInferior2'
    const inputs2 = document.querySelectorAll("#miembroFormInferior2 input");
    inputs2.forEach(input => {
        input.addEventListener("input", saveFormDataInferior2);
    });

    // Guardar datos en tiempo real para 'miembroFormInferior3'
    const inputs3 = document.querySelectorAll("#miembroFormInferior3 input");
    inputs3.forEach(input => {
        input.addEventListener("input", saveFormDataInferior3);
    });

    // Guardar datos en tiempo real para 'miembroFormInferior4'
    const inputs4 = document.querySelectorAll("#miembroFormInferior4 input");
    inputs4.forEach(input => {
        input.addEventListener("input", saveFormDataInferior4);
    });

    // Guardar datos en tiempo real para 'miembroFormInferior5'
    const inputs5 = document.querySelectorAll("#miembroFormInferior5 input");
    inputs5.forEach(input => {
        input.addEventListener("input", saveFormDataInferior5);
    });
});

// Función para establecer el valor de un campo de texto o marcar un checkbox
const establecerValor = (id, valor) => {
    const elemento =
      document.getElementById(id) ||
      document.querySelector(`input[name="${id}"]`);
    if (elemento) {
      if (elemento.type === "checkbox") {
        elemento.checked = valor === 1; // Marcar o desmarcar el checkbox
      } else {
        elemento.value = valor || "No hay información";
      }
    }
  }; 
  
  // Consultar el Id desde el localStorage
  const id = localStorage.getItem("Id");
  
  console.log("El Id almacenado es:", id);

  if (id) {
    fetch('/consultarMiembrosInferiores', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ id: id }),
    })
      .then(response => response.json())
      .then(data => {
        if (data.error) {
          console.error("Error desde el servidor:", data.error);
          return;
        }
  
        console.log("Datos recibidos:", data);
  
        // Actualizar los campos en el DOM con los datos obtenidos
        establecerValor("observacionesMiembrosInferiores", data.observacionesMiembrosInferiores);
        establecerValor("palpacionMiembrosInferiores", data.palpacionMiembrosInferiores);
        establecerValor("dolorSuperiorMiembrosInferiores", data.dolorSuperiorMiembrosInferiores);
        establecerValor("dolorexplofisicaMiembrosInferiores", data.dolorexplofisicaMiembrosInferiores);
      })
      .catch(error => {
        console.error("Error al consultar los datos:", error);
      });
  } else {
    console.error("No se encontró un ID en el localStorage");
  }
  
  if (id) {
    fetch('/consultarFuerzaMuscularMiembrosInferiores', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ id: id }),
    })
      .then(response => response.json())
      .then(data => {
        if (data.error) {
          console.error("Error desde el servidor:", data.error);
          return;
        }
  
        console.log("Datos recibidos:", data);
  
        // Actualizar los campos en el DOM con los datos obtenidos
        data.forEach(fuerza => {
          const { movimiento, izquierda, derecha } = fuerza;
  
          // Actualizar valores de los campos izquierdo y derecho
          establecerValor(`${movimiento}_izquierdo`, izquierda);
          establecerValor(`${movimiento}_derecho`, derecha);
        });
      })
      .catch(error => {
        console.error("Error al consultar los datos:", error);
      });
  } else {
    console.error("No se encontró un ID en el localStorage");
  }
  
  if (id) {
    fetch('/consultarGoniometriaMiembrosInferiores', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ id: id }),
    })
      .then(response => response.json())
      .then(data => {
        if (data.error) {
          console.error("Error desde el servidor:", data.error);
          return;
        }
  
        console.log("Datos recibidos:", data);
  
        // Actualizar los campos en el DOM con los datos obtenidos
        data.forEach(goniometria => {
          const { rango, movimiento, izquierdo, derecho } = goniometria;
  
          // Actualizar valores de los campos izquierdo y derecho
          establecerValor(`${rango}_${movimiento}_izquierdo`, izquierdo);
          establecerValor(`${rango}_${movimiento}_derecho`, derecho);
        });
      })
      .catch(error => {
        console.error("Error al consultar los datos:", error);
      });
  } else {
    console.error("No se encontró un ID en el localStorage");
  }
  
  if (id) {
    fetch('/consultarReflejosOsteotendinososMiembrosInferiores', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ id: id }),
    })
      .then(response => response.json())
      .then(data => {
        if (data.error) {
          console.error("Error desde el servidor:", data.error);
          return;
        }
  
        console.log("Datos recibidos:", data);
  
        // Actualizar los campos en el DOM con los datos obtenidos
        data.forEach(reflejo => {
          const { reflejo: nombreReflejo, izquierdo, derecho } = reflejo;
  
          // Actualizar valores de los campos izquierdo y derecho
          establecerValor(`${nombreReflejo}_izq`, izquierdo);
          establecerValor(`${nombreReflejo}_der`, derecho);
        });
      })
      .catch(error => {
        console.error("Error al consultar los datos:", error);
      });
  } else {
    console.error("No se encontró un ID en el localStorage");
  }
  
  if (id) {
    fetch('/consultarPruebasEvaluacionesComplementariasInferiores', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ id: id }),
    })
      .then(response => response.json())
      .then(data => {
        if (data.error) {
          console.error("Error desde el servidor:", data.error);
          return;
        }
  
        console.log("Datos recibidos:", data);
  
        // Actualizar los campos en el DOM con los datos obtenidos
        data.forEach((prueba, index) => {
          const { prueba: pruebaName, resultado } = prueba;
  
          // Actualizar valores de las pruebas y resultados por índice
          establecerValor(`Pruebas_${index + 1}_MiembrosInferiores`, pruebaName);
          establecerValor(`Resultados y análisis_${index + 1}_MiembrosInferiores`, resultado);
        });
      })
      .catch(error => {
        console.error("Error al consultar los datos:", error);
      });
  } else {
    console.error("No se encontró un ID en el localStorage");
  }
  
  if (id) {
    fetch('/consultarCicloMarchaMiembrosInferiores', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ id: id }),
    })
      .then(response => response.json())
      .then(data => {
        if (data.error) {
          console.error("Error desde el servidor:", data.error);
          return;
        }
  
        console.log("Datos recibidos:", data);
  
        // Asignar los valores directamente al DOM utilizando los nombres de los campos
        establecerValor("Fase_de_apoyo_completo", data.faseApoyoCompleto);
        establecerValor("Contacto_de_talon_izquierdo", data.contactoTalonIzquierdo);
        establecerValor("Contacto_de_talon_derecho", data.contactoTalonDerecho);
        establecerValor("Apoyo_plantar_izquierdo", data.apoyoPlantarIzquierdo);
        establecerValor("Apoyo_plantar_derecho", data.apoyoPlantarDerecho);
        establecerValor("Apoyo_medio_izquierdo", data.apoyoMedioIzquierdo);
        establecerValor("Apoyo_medio_derecho", data.apoyoMedioDerecho);
        establecerValor("Fase_de_oscilacion_completo", data.faseOscilacionCompleto);
        establecerValor("Balanceo_inicial_izquierdo", data.balanceoInicialIzquierdo);
        establecerValor("Balanceo_inicial_derecho", data.balanceoInicialDerecho);
        establecerValor("Balanceo_medio_izquierdo", data.balanceoMedioIzquierdo);
        establecerValor("Balanceo_medio_derecho", data.balanceoMedioDerecho);
        establecerValor("Balanceo_terminal_izquierdo", data.balanceoTerminalIzquierdo);
        establecerValor("Balanceo_terminal_derecho", data.balanceoTerminalDerecho);
        establecerValor("Rotacion_pelvica_completo", data.rotacionPelvicaCompleto);
        establecerValor("Inclinacion_pelvica_completo", data.inclinacionPelvicaCompleto);
        establecerValor("Flexion_de_rodilla_izquierdo", data.flexionRodillaIzquierdo);
        establecerValor("Flexion_de_rodilla_derecho", data.flexionRodillaDerecho);
        establecerValor("Movimientos_coordinados_de_rodilla_y_tobillo_izquierdo", data.movimientosCoordinadosRodillaTobilloIzquierdo);
        establecerValor("Movimientos_coordinados_de_rodilla_y_tobillo_derecho", data.movimientosCoordinadosRodillaTobilloDerecho);
        establecerValor("Movimiento_del_centro_de_gravedad_completo", data.movimientoCentroGravedadCompleto);
        establecerValor("Cadencia_completo", data.cadenciaCompleto);
        establecerValor("Balanceo_de_MS_completo", data.balanceoMSCompleto);
      })
      .catch(error => {
        console.error("Error al consultar los datos:", error);
      });
  } else {
    console.error("No se encontró un ID en el localStorage");
  }
  
  