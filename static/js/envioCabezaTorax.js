// Función para obtener el valor de un campo de texto
const obtenerValor = id => document.getElementById(id)?.value || 'No hay información';
const obtenerValorNumerico = id => parseFloat(document.getElementById(id)?.value) || 0;
const obtenerValorEntero = id => parseInt(document.getElementById(id)?.value, 10) || 0;


function guardarDatosCabezaTorax() {
    const datosCabezaTorax = {
        // Cabeza y Toráx
        // // Cabeza y Toráx
        observacionesCabezaCuello: obtenerValor('observacionesCabezaCuello'),
        palpacionCabezaCuello: obtenerValor('palpacionCabezaCuello'),
        dolorSuperiorCabezaCuello: obtenerValor('dolorSuperiorCabezaCuello'),
        dolorexplofisicaCabezaCuello: obtenerValorEntero('dolorexplofisicaCabezaCuello'),
        // Fuerza Muscular
        fuerzaMuscularCabezaTorax1: ['Extensión de cabeza', 'Extensión de cuello', 'Extensión conjunta', 'Flexión de cabeza',
            'Flexión de cuello', 'Flexión conjunta', 'Flexión y rotación conjuntas', 'Rotación del cuello', 'Observaciones'
        ].map(movimiento => ({
            movimiento,
            valoresObtenidos: document.querySelector(`input[name="${movimiento}_valoresObtenidos"]`)?.value || 'No hay información',
        })),
        // Columna, tórax y abdomen
        observacionesColumnaTóraxAbdomen: obtenerValor('observacionesColumnaTóraxAbdomen'),
        palpacionColumnaTóraxAbdomen: obtenerValor('palpacionColumnaTóraxAbdomen'),
        dolorSuperiorColumnaTóraxAbdomen: obtenerValor('dolorSuperiorColumnaTóraxAbdomen'),
        dolorexplofisicaColumnaTóraxAbdomen: obtenerValorEntero('dolorexplofisicaColumnaTóraxAbdomen'),
        // Fuerza Muscular
        fuerzaMuscularCabezaTorax2: ['Extensión lumbar', 'Extensión torácica', 'Elevación pélvica', 'Flexión',
            'Rotación', 'Inspiración', 'Espiración forzada indirecta'
        ].map(movimiento => ({
            movimiento,
            valoresObtenidos: document.querySelector(`input[name="${movimiento}_valoresObtenidos"]`)?.value || 'No hay información',
        })),
        // Goniometría
        goniometriaCabezaTorax: [
            { rango: '0-35°/45°', movimiento: 'Flexión' }, { rango: '0-35°/45°', movimiento: 'Extensión' },
            { rango: '0°-45°', movimiento: 'Inclinación lateral derecha' }, { rango: '0°-45°', movimiento: 'Inclinación lateral izquierda' },
            { rango: '0-60°/80°', movimiento: 'Rotación derecha' }, { rango: '0-60°/80°', movimiento: 'Rotación izquierda' },
            { rango: '*método de Schober', movimiento: 'Flexión' }, { rango: '0-30°', movimiento: 'Extensión' },
            { rango: '0-30°/40°', movimiento: 'Inclinación lateral derecha' }, { rango: '0°-30°/40°', movimiento: 'Inclinación lateral izquierda' },
            { rango: '0-30°', movimiento: 'Rotación derecha' }, { rango: '0-30°', movimiento: 'Rotación izquierda' }
        ].map(rangoMovimiento => ({
            ...rangoMovimiento,
            resultados: document.querySelector(`input[name="${rangoMovimiento.rango}_${rangoMovimiento.movimiento}_resultados"]`)?.value || 'No hay información',
        })),
        // Pruebas y Evaluaciones Complementarias
        pruebasEvaluacionesComplementariasCabezaTorax: [
            '1',
            '2',
            '3',
            '4'
        ].map((numero) => ({
            prueba: document.querySelector(`input[name="Pruebas_${numero}_CabezaTorax"]`)?.value || 'No hay información',
            resultado: document.querySelector(`input[name="Resultados y análisis_${numero}_CabezaTorax"]`)?.value || 'No hay información',
        })),
    };
    localStorage.setItem('datosCabezaTorax', JSON.stringify(datosCabezaTorax));
}

document.getElementById('miembroFormCabezaTorax').addEventListener('submit', function (event) {
    event.preventDefault();
    guardarDatosCabezaTorax();
    window.location.href = '/EvaluacionDeLaPostura'; // Redirige a la página de resumen
});

document.querySelectorAll('input, select, textarea').forEach(element => {
    element.addEventListener('change', guardarDatosCabezaTorax);
});

// Obtener los botones por su ID
const botonVisible = document.getElementById('botonVisible');
const botonOculto = document.getElementById('botonOculto');
// Agregar un evento de clic al botón visible
botonVisible.addEventListener('click', function () {
    // Disparar el evento de clic del botón oculto
    botonOculto.click();
});

// ------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function () {

    // Función para guardar los datos del formulario 'miembroFormCabezaTorax' en localStorage
    function saveFormDataCabezaTorax() {
        const formData = {};
        const inputs = document.querySelectorAll("#miembroFormCabezaTorax input, #miembroFormCabezaTorax textarea");
        inputs.forEach(input => {
            formData[input.id] = input.value;
        });
        localStorage.setItem("miembroFormCabezaToraxData", JSON.stringify(formData));
    }

    // Función para cargar los datos del formulario 'miembroFormCabezaTorax' desde localStorage
    function loadFormDataCabezaTorax() {
        const formData = JSON.parse(localStorage.getItem("miembroFormCabezaToraxData"));
        if (formData) {
            const inputs = document.querySelectorAll("#miembroFormCabezaTorax input, #miembroFormCabezaTorax textarea");
            inputs.forEach(input => {
                if (formData[input.id]) {
                    input.value = formData[input.id];
                }
            });
        }
    }

    // Función para guardar los datos del formulario 'miembroFormCabezaTorax1' en localStorage
    function saveFormDataCabezaTorax1() {
        const formData1 = {};
        const inputs1 = document.querySelectorAll("#miembroFormCabezaTorax1 input");
        inputs1.forEach(input => {
            formData1[input.name] = input.value;
        });
        localStorage.setItem("miembroFormCabezaTorax1Data", JSON.stringify(formData1));
    }

    // Función para cargar los datos del formulario 'miembroFormCabezaTorax1' desde localStorage
    function loadFormDataCabezaTorax1() {
        const formData1 = JSON.parse(localStorage.getItem("miembroFormCabezaTorax1Data"));
        if (formData1) {
            const inputs1 = document.querySelectorAll("#miembroFormCabezaTorax1 input");
            inputs1.forEach(input => {
                if (formData1[input.name]) {
                    input.value = formData1[input.name];
                }
            });
        }
    }

    // Función para guardar los datos del formulario 'miembroFormCabezaTorax2' en localStorage
    function saveFormDataCabezaTorax2() {
        const formData2 = {};
        const inputs2 = document.querySelectorAll("#miembroFormCabezaTorax2 input, #miembroFormCabezaTorax2 textarea");
        inputs2.forEach(input => {
            formData2[input.id] = input.value;
        });
        localStorage.setItem("miembroFormCabezaTorax2Data", JSON.stringify(formData2));
    }

    // Función para cargar los datos del formulario 'miembroFormCabezaTorax2' desde localStorage
    function loadFormDataCabezaTorax2() {
        const formData2 = JSON.parse(localStorage.getItem("miembroFormCabezaTorax2Data"));
        if (formData2) {
            const inputs2 = document.querySelectorAll("#miembroFormCabezaTorax2 input, #miembroFormCabezaTorax2 textarea");
            inputs2.forEach(input => {
                if (formData2[input.id]) {
                    input.value = formData2[input.id];
                }
            });
        }
    }

    // Función para guardar los datos del formulario 'miembroFormCabezaTorax3' en localStorage
    function saveFormDataCabezaTorax3() {
        const formData3 = {};
        const inputs3 = document.querySelectorAll("#miembroFormCabezaTorax3 input");
        inputs3.forEach(input => {
            formData3[input.name] = input.value;
        });
        localStorage.setItem("miembroFormCabezaTorax3Data", JSON.stringify(formData3));
    }

    // Función para cargar los datos del formulario 'miembroFormCabezaTorax3' desde localStorage
    function loadFormDataCabezaTorax3() {
        const formData3 = JSON.parse(localStorage.getItem("miembroFormCabezaTorax3Data"));
        if (formData3) {
            const inputs3 = document.querySelectorAll("#miembroFormCabezaTorax3 input");
            inputs3.forEach(input => {
                if (formData3[input.name]) {
                    input.value = formData3[input.name];
                }
            });
        }
    }

    // Función para guardar los datos del formulario 'miembroFormCabezaTorax4' en localStorage
    function saveFormDataCabezaTorax4() {
        const formData4 = {};
        const inputs4 = document.querySelectorAll("#miembroFormCabezaTorax4 input");
        inputs4.forEach(input => {
            formData4[input.name] = input.value;
        });
        localStorage.setItem("miembroFormCabezaTorax4Data", JSON.stringify(formData4));
    }

    // Función para cargar los datos del formulario 'miembroFormCabezaTorax4' desde localStorage
    function loadFormDataCabezaTorax4() {
        const formData4 = JSON.parse(localStorage.getItem("miembroFormCabezaTorax4Data"));
        if (formData4) {
            const inputs4 = document.querySelectorAll("#miembroFormCabezaTorax4 input");
            inputs4.forEach(input => {
                if (formData4[input.name]) {
                    input.value = formData4[input.name];
                }
            });
        }
    }

    // Función para guardar los datos del formulario 'miembroFormCabezaTorax5' en localStorage
    function saveFormDataCabezaTorax5() {
        const formData5 = {};
        const inputs5 = document.querySelectorAll("#miembroFormCabezaTorax5 input");
        inputs5.forEach(input => {
            formData5[input.name] = input.value;
        });
        localStorage.setItem("miembroFormCabezaTorax5Data", JSON.stringify(formData5));
    }

    // Función para cargar los datos del formulario 'miembroFormCabezaTorax5' desde localStorage
    function loadFormDataCabezaTorax5() {
        const formData5 = JSON.parse(localStorage.getItem("miembroFormCabezaTorax5Data"));
        if (formData5) {
            const inputs5 = document.querySelectorAll("#miembroFormCabezaTorax5 input");
            inputs5.forEach(input => {
                if (formData5[input.name]) {
                    input.value = formData5[input.name];
                }
            });
        }
    }

    // Cargar datos al cargar la página
    loadFormDataCabezaTorax();
    loadFormDataCabezaTorax1();
    loadFormDataCabezaTorax2();
    loadFormDataCabezaTorax3();
    loadFormDataCabezaTorax4();
    loadFormDataCabezaTorax5();

    // Guardar datos en tiempo real para 'miembroFormCabezaTorax'
    const inputs = document.querySelectorAll("#miembroFormCabezaTorax input, #miembroFormCabezaTorax textarea");
    inputs.forEach(input => {
        input.addEventListener("input", saveFormDataCabezaTorax);
    });

    // Guardar datos en tiempo real para 'miembroFormCabezaTorax1'
    const inputs1 = document.querySelectorAll("#miembroFormCabezaTorax1 input");
    inputs1.forEach(input => {
        input.addEventListener("input", saveFormDataCabezaTorax1);
    });

    // Guardar datos en tiempo real para 'miembroFormCabezaTorax2'
    const inputs2 = document.querySelectorAll("#miembroFormCabezaTorax2 input, #miembroFormCabezaTorax2 textarea");
    inputs2.forEach(input => {
        input.addEventListener("input", saveFormDataCabezaTorax2);
    });

    // Guardar datos en tiempo real para 'miembroFormCabezaTorax3'
    const inputs3 = document.querySelectorAll("#miembroFormCabezaTorax3 input");
    inputs3.forEach(input => {
        input.addEventListener("input", saveFormDataCabezaTorax3);
    });

    // Guardar datos en tiempo real para 'miembroFormCabezaTorax4'
    const inputs4 = document.querySelectorAll("#miembroFormCabezaTorax4 input");
    inputs4.forEach(input => {
        input.addEventListener("input", saveFormDataCabezaTorax4);
    });

    // Guardar datos en tiempo real para 'miembroFormCabezaTorax5'
    const inputs5 = document.querySelectorAll("#miembroFormCabezaTorax5 input");
    inputs5.forEach(input => {
        input.addEventListener("input", saveFormDataCabezaTorax5);
    });
});