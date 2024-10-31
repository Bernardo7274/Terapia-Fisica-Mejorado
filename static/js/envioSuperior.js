// Función para obtener el valor de un campo de texto
const obtenerValor = id => document.getElementById(id)?.value || 'No hay información';
const obtenerValorNumerico = id => parseFloat(document.getElementById(id)?.value) || 0;
const obtenerValorEntero = id => parseInt(document.getElementById(id)?.value, 10) || 0;


function guardarDatosMiembroSuperior() {
    const datosMiembroSuperior = {
        // Miembros Superiores
        observacionesMiembrosSuperiores: obtenerValor('observacionesMiembrosSuperiores'),
        palpacionMiembrosSuperiores: obtenerValor('palpacionMiembrosSuperiores'),
        dolorSuperiorMiembrosSuperiores: obtenerValor('dolorSuperiorMiembrosSuperiores'),
        dolorexplofisicaMiembrosSuperiores: obtenerValorEntero('dolorexplofisicaMiembrosSuperiores'),
        // Fuerza Muscular
        fuerzaMuscularMiembrosSuperiores: ['Abducción y rotación superior de la escápula', 'Elevación de la escápula', 'Aducción de la escápula', 'Aducción y descenso escapular',
            'Aducción y rotación inferior de la escápula', 'Flexión del hombro', 'Extensión de hombro', 'Abducción del hombro', 'Abducción horizontal del hombro',
            'Aducción horizontal del hombro', 'Rotación externa del hombro', 'Rotación interna del hombro', 'Flexión de codo', 'Extensión de codo',
            'Supinación del antebrazo', 'Pronación del antebrazo', 'Flexión de la muñeca', 'Extensión de la muñeca'
        ].map(movimiento => ({
            movimiento,
            izquierdo: document.querySelector(`input[name="${movimiento}_izquierdo"]`)?.value || 'No hay información',
            derecho: document.querySelector(`input[name="${movimiento}_derecho"]`)?.value || 'No hay información',
        })),
        // Goniometría
        goniometriaMiembrosSuperiores: [
            { rango: '0°-150°/170°', movimiento: 'Flexión de hombro' }, { rango: '0°-40°', movimiento: 'Extensión de hombro' },
            { rango: '0-160°/180°', movimiento: 'Abducción de hombro' }, { rango: '0°-30°', movimiento: 'Aducción de hombro' },
            { rango: '0°-70°', movimiento: 'Rotación externa de hombro' }, { rango: '0°-70°', movimiento: 'Rotación interna de hombro' },
            { rango: '0°-150°', movimiento: 'Flexión de codo' }, { rango: '0°(activa)-10°(pasiva)', movimiento: 'Extensión de codo' },
            { rango: '0°-90°', movimiento: 'Supinación del antebrazo' }, { rango: '0°-90°', movimiento: 'Pronación del antebrazo' },
            { rango: '0°-25°-30°', movimiento: 'Desviación radial de muñeca' }, { rango: '0°-30°-40°', movimiento: 'Desviación cubital de la muñeca' },
            { rango: '0°-50°/60°', movimiento: 'Flexión de muñeca' }, { rango: '0°-35°/60°', movimiento: 'Extensión de muñeca' }
        ].map(rangoMovimiento => ({
            ...rangoMovimiento,
            izquierdo: document.querySelector(`input[name="${rangoMovimiento.rango}_${rangoMovimiento.movimiento}_izquierdo"]`)?.value || 'No hay información',
            derecho: document.querySelector(`input[name="${rangoMovimiento.rango}_${rangoMovimiento.movimiento}_derecho"]`)?.value || 'No hay información',
        })),
        // Reflejos Osteotendinosos
        reflejosOsteotendinososMiembrosSuperiores: [
            'Bicipital', 'Tricipital', 'Braquioradial', 'Estiloradial'
        ].map(reflejo => ({
            reflejo,
            izquierdo: document.querySelector(`input[name="${reflejo}_izq"]`)?.value || 'No hay información',
            derecho: document.querySelector(`input[name="${reflejo}_der"]`)?.value || 'No hay información',
        })),
        // Pruebas y Evaluaciones Complementarias
        pruebasEvaluacionesComplementariasMiembrosSuperiores: [
            '1',
            '2',
            '3',
            '4'
        ].map((numero) => ({
            prueba: document.querySelector(`input[name="Pruebas_${numero}_MiembrosSuperiores"]`)?.value || 'No hay información',
            resultado: document.querySelector(`input[name="Resultados y análisis_${numero}_MiembrosSuperiores"]`)?.value || 'No hay información',
        }))
    };
    localStorage.setItem('datosMiembroSuperior', JSON.stringify(datosMiembroSuperior));
}

document.getElementById('miembroFormSuperior').addEventListener('submit', function (event) {
    event.preventDefault();
    guardarDatosMiembroSuperior();
    window.location.href = '/MiembroInferior'; // Redirige a la página de resumen
});

document.querySelectorAll('input, select, textarea').forEach(element => {
    element.addEventListener('change', guardarDatosMiembroSuperior);
});

// Obtener los botones por su ID
const botonVisible = document.getElementById('botonVisible');
const botonOculto = document.getElementById('botonOculto');
// Agregar un evento de clic al botón visible
botonVisible.addEventListener('click', function () {
    // Disparar el evento de clic del botón oculto
    botonOculto.click();
});

// ------------------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function () {

    // Función para guardar los datos del formulario 'miembroFormSuperior' en localStorage
    function saveFormData7() {
        const formData7 = {};
        const inputs7 = document.querySelectorAll("#miembroFormSuperior input, #miembroFormSuperior textarea");
        inputs7.forEach(input => {
            formData7[input.id] = input.value;
        });
        localStorage.setItem("miembroFormSuperiorData", JSON.stringify(formData7));
    }

    // Función para cargar los datos del formulario 'miembroFormSuperior' desde localStorage
    function loadFormData7() {
        const formData7 = JSON.parse(localStorage.getItem("miembroFormSuperiorData"));
        if (formData7) {
            const inputs7 = document.querySelectorAll("#miembroFormSuperior input, #miembroFormSuperior textarea");
            inputs7.forEach(input => {
                if (formData7[input.id]) {
                    input.value = formData7[input.id];
                }
            });
        }
    }

    // Función para guardar los datos del formulario 'miembroFormSuperior1' en localStorage
    function saveFormData8() {
        const formData8 = {};
        const inputs8 = document.querySelectorAll("#miembroFormSuperior1 input");
        inputs8.forEach(input => {
            formData8[input.id] = input.value;
        });
        localStorage.setItem("miembroFormSuperior1Data", JSON.stringify(formData8));
    }

    // Función para cargar los datos del formulario 'miembroFormSuperior1' desde localStorage
    function loadFormData8() {
        const formData8 = JSON.parse(localStorage.getItem("miembroFormSuperior1Data"));
        if (formData8) {
            const inputs8 = document.querySelectorAll("#miembroFormSuperior1 input");
            inputs8.forEach(input => {
                if (formData8[input.id]) {
                    input.value = formData8[input.id];
                }
            });
        }
    }

    // Función para guardar los datos del formulario 'miembroFormSuperior2' en localStorage
    function saveFormData9() {
        const formData9 = {};
        const inputs9 = document.querySelectorAll("#miembroFormSuperior2 input");
        inputs9.forEach(input => {
            formData9[input.name] = input.value;
        });
        localStorage.setItem("miembroFormSuperior2Data", JSON.stringify(formData9));
    }

    // Función para cargar los datos del formulario 'miembroFormSuperior2' desde localStorage
    function loadFormData9() {
        const formData9 = JSON.parse(localStorage.getItem("miembroFormSuperior2Data"));
        if (formData9) {
            const inputs9 = document.querySelectorAll("#miembroFormSuperior2 input");
            inputs9.forEach(input => {
                if (formData9[input.name]) {
                    input.value = formData9[input.name];
                }
            });
        }
    }

    // Función para guardar los datos del formulario 'miembroFormSuperior3' en localStorage
    function saveFormData10() {
        const formData10 = {};
        const inputs10 = document.querySelectorAll("#miembroFormSuperior3 input");
        inputs10.forEach(input => {
            formData10[input.name] = input.value;
        });
        localStorage.setItem("miembroFormSuperior3Data", JSON.stringify(formData10));
    }

    // Función para cargar los datos del formulario 'miembroFormSuperior3' desde localStorage
    function loadFormData10() {
        const formData10 = JSON.parse(localStorage.getItem("miembroFormSuperior3Data"));
        if (formData10) {
            const inputs10 = document.querySelectorAll("#miembroFormSuperior3 input");
            inputs10.forEach(input => {
                if (formData10[input.name]) {
                    input.value = formData10[input.name];
                }
            });
        }
    }

    // Función para guardar los datos del formulario 'miembroFormSuperior4' en localStorage
    function saveFormData11() {
        const formData11 = {};
        const inputs11 = document.querySelectorAll("#miembroFormSuperior4 input");
        inputs11.forEach(input => {
            formData11[input.name] = input.value;
        });
        localStorage.setItem("miembroFormSuperior4Data", JSON.stringify(formData11));
    }

    // Función para cargar los datos del formulario 'miembroFormSuperior4' desde localStorage
    function loadFormData11() {
        const formData11 = JSON.parse(localStorage.getItem("miembroFormSuperior4Data"));
        if (formData11) {
            const inputs11 = document.querySelectorAll("#miembroFormSuperior4 input");
            inputs11.forEach(input => {
                if (formData11[input.name]) {
                    input.value = formData11[input.name];
                }
            });
        }
    }

    // Cargar datos al cargar la página
    loadFormData7();
    loadFormData8();
    loadFormData9();
    loadFormData10();
    loadFormData11();

    // Guardar datos en tiempo real para 'miembroFormSuperior'
    const inputs7 = document.querySelectorAll("#miembroFormSuperior input, #miembroFormSuperior textarea");
    inputs7.forEach(input => {
        input.addEventListener("input", saveFormData7);
    });

    // Guardar datos en tiempo real para 'miembroFormSuperior1'
    const inputs8 = document.querySelectorAll("#miembroFormSuperior1 input");
    inputs8.forEach(input => {
        input.addEventListener("input", saveFormData8);
    });

    // Guardar datos en tiempo real para 'miembroFormSuperior2'
    const inputs9 = document.querySelectorAll("#miembroFormSuperior2 input");
    inputs9.forEach(input => {
        input.addEventListener("input", saveFormData9);
    });

    // Guardar datos en tiempo real para 'miembroFormSuperior3'
    const inputs10 = document.querySelectorAll("#miembroFormSuperior3 input");
    inputs10.forEach(input => {
        input.addEventListener("input", saveFormData10);
    });

    // Guardar datos en tiempo real para 'miembroFormSuperior4'
    const inputs11 = document.querySelectorAll("#miembroFormSuperior4 input");
    inputs11.forEach(input => {
        input.addEventListener("input", saveFormData11);
    });
});
