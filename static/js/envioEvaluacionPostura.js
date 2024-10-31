// Función para obtener el valor de un campo de texto
const obtenerValor = id => document.getElementById(id)?.value || 'No hay información';
const obtenerValorNumerico = id => parseFloat(document.getElementById(id)?.value) || 0;
const obtenerValorEntero = id => parseInt(document.getElementById(id)?.value, 10) || 0;


function guardarDatosEvaluacionPostura() {
    const datosEvaluacionPostura = {
        // Evaluación de la postura
        // Vista frontal
        vistaFrontal: ['Cabeza', 'Hombros', 'Miembros Superiores', 'Tronco',
            'Cadera', 'Rodillas', 'Pies'
        ].map(alineacionCorporal => ({
            alineacionCorporal,
            ObservacionesvistaFrontal: document.querySelector(`input[name="${alineacionCorporal}_ob"]`)?.value || 'No hay información',
        })),
        // Vista lateral
        vistaLateral: ['Cabeza', 'Hombros', 'Miembros Superiores', 'Tronco',
            'Cadera', 'Rodillas', 'Pies'
        ].map(alineacionCorporal1 => ({
            alineacionCorporal1,
            ObservacionesvistaLateral: document.querySelector(`input[name="${alineacionCorporal1}_ob1"]`)?.value || 'No hay información',
        })),
        // Vista posterior
        vistaPosterior: ['Cabeza', 'Hombros', 'Miembros Superiores', 'Tronco',
            'Cadera', 'Rodillas', 'Pies'
        ].map(alineacionCorporal2 => ({
            alineacionCorporal2,
            ObservacionesvistaPosterior: document.querySelector(`input[name="${alineacionCorporal2}_ob2"]`)?.value || 'No hay información',
        })),
    };
    localStorage.setItem('datosEvaluacionPostura', JSON.stringify(datosEvaluacionPostura));
}

document.getElementById('miembroEvaluacionPostura').addEventListener('submit', function (event) {
    event.preventDefault();
    guardarDatosEvaluacionPostura();
    window.location.href = '/NotasSeguimiento'; // Redirige a la página de resumen
});

document.querySelectorAll('input, select, textarea').forEach(element => {
    element.addEventListener('change', guardarDatosEvaluacionPostura);
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
    // Función para guardar los datos del formulario en localStorage
    function saveFormData12() {
        const formData12 = {};
        const inputs12 = document.querySelectorAll("#miembroEvaluacionPostura input");
        inputs12.forEach(input => {
            formData12[input.name] = input.value;
        });
        localStorage.setItem("miembroEvaluacionPosturaData", JSON.stringify(formData12));
    }

    // Función para cargar los datos del formulario desde localStorage
    function loadFormData12() {
        const formData12 = JSON.parse(localStorage.getItem("miembroEvaluacionPosturaData"));
        if (formData12) {
            const inputs12 = document.querySelectorAll("#miembroEvaluacionPostura input");
            inputs12.forEach(input => {
                if (formData12[input.name]) {
                    input.value = formData12[input.name];
                }
            });
        }
    }

    // Función para guardar los datos del segundo formulario en localStorage
    function saveFormData13() {
        const formData13 = {};
        const inputs13 = document.querySelectorAll("#miembroEvaluacionPostura1 input");
        inputs13.forEach(input => {
            formData13[input.name] = input.value;
        });
        localStorage.setItem("miembroEvaluacionPostura1Data", JSON.stringify(formData13));
    }

    // Función para cargar los datos del segundo formulario desde localStorage
    function loadFormData13() {
        const formData13 = JSON.parse(localStorage.getItem("miembroEvaluacionPostura1Data"));
        if (formData13) {
            const inputs13 = document.querySelectorAll("#miembroEvaluacionPostura1 input");
            inputs13.forEach(input => {
                if (formData13[input.name]) {
                    input.value = formData13[input.name];
                }
            });
        }
    }

    // Función para guardar los datos del tercer formulario en localStorage
    function saveFormData14() {
        const formData14 = {};
        const inputs14 = document.querySelectorAll("#miembroEvaluacionPostura2 input");
        inputs14.forEach(input => {
            formData14[input.name] = input.value;
        });
        localStorage.setItem("miembroEvaluacionPostura2Data", JSON.stringify(formData14));
    }

    // Función para cargar los datos del tercer formulario desde localStorage
    function loadFormData14() {
        const formData14 = JSON.parse(localStorage.getItem("miembroEvaluacionPostura2Data"));
        if (formData14) {
            const inputs14 = document.querySelectorAll("#miembroEvaluacionPostura2 input");
            inputs14.forEach(input => {
                if (formData14[input.name]) {
                    input.value = formData14[input.name];
                }
            });
        }
    }

    // Cargar datos al cargar la página
    loadFormData12();
    loadFormData13();
    loadFormData14();

    // Guardar datos en tiempo real para "Vista Frontal"
    const inputs12 = document.querySelectorAll("#miembroEvaluacionPostura input");
    inputs12.forEach(input => {
        input.addEventListener("input", saveFormData12);
    });

    // Guardar datos en tiempo real para "Vista Lateral"
    const inputs13 = document.querySelectorAll("#miembroEvaluacionPostura1 input");
    inputs13.forEach(input => {
        input.addEventListener("input", saveFormData13);
    });

    // Guardar datos en tiempo real para "Vista Posterior"
    const inputs14 = document.querySelectorAll("#miembroEvaluacionPostura2 input");
    inputs14.forEach(input => {
        input.addEventListener("input", saveFormData14);
    });
});
