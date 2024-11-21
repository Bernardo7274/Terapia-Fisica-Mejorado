const obtenerValor = id => document.getElementById(id)?.value || 'No hay información';
const obtenerValorNumerico = id => parseFloat(document.getElementById(id)?.value) || 0;
const obtenerValorEntero = id => parseInt(document.getElementById(id)?.value, 10) || 0;

function guardarDatosDiagnostico() {
    const filasPlanTratamiento = document.querySelectorAll('#miembroPlanDiagnostico tbody tr');
    const planTratamiento = Array.from(filasPlanTratamiento).map((fila, index) => ({
        objetivo: fila.querySelector(`textarea[name="objetivo_${index + 1}_planDiagnostico"]`).value,
        modalidad: fila.querySelector(`textarea[name="modalidad_${index + 1}_planDiagnostico"]`).value,
        descripcion: fila.querySelector(`textarea[name="descripcion_${index + 1}_planDiagnostico"]`).value,
        dosis: fila.querySelector(`textarea[name="dosis_${index + 1}_planDiagnostico"]`).value
    }));

    const datosDiagnostico = { planTratamiento };
    localStorage.setItem('datosDiagnostico', JSON.stringify(datosDiagnostico));
}

document.getElementById('miembroPlanDiagnostico').addEventListener('submit', function (event) {
    event.preventDefault();
    guardarDatosDiagnostico();
    window.location.href = '/Resumen';
});

document.querySelectorAll('textarea').forEach(element => {
    element.addEventListener('change', guardarDatosDiagnostico1);
});

// Función para guardar los datos de la tabla en el localStorage
function guardarDatosDiagnostico1() {
    const filas = [];
    document.querySelectorAll('#miembroPlanDiagnostico tbody tr').forEach((tr, index) => {
        const fila = {
            objetivo: tr.querySelector(`textarea[name="objetivo_${index + 1}_planDiagnostico"]`).value,
            modalidad: tr.querySelector(`textarea[name="modalidad_${index + 1}_planDiagnostico"]`).value,
            descripcion: tr.querySelector(`textarea[name="descripcion_${index + 1}_planDiagnostico"]`).value,
            dosis: tr.querySelector(`textarea[name="dosis_${index + 1}_planDiagnostico"]`).value
        };
        filas.push(fila);
    });

    // Guardar las filas en el localStorage
    localStorage.setItem('filasDiagnostico', JSON.stringify(filas));
}

// Función para cargar los datos guardados del localStorage
function cargarDatosDiagnostico() {
    const filasGuardadas = JSON.parse(localStorage.getItem('filasDiagnostico'));
    if (filasGuardadas) {
        const tableBody = document.querySelector('#miembroPlanDiagnostico tbody');
        tableBody.innerHTML = ''; // Limpiar el contenido actual

        // Añadir filas guardadas
        filasGuardadas.forEach((fila, index) => {
            const newRow = document.createElement('tr');
            newRow.innerHTML = `
                <td><textarea class="form-control" name="objetivo_${index + 1}_planDiagnostico" style="height: 100px; min-width: 100px;" placeholder="">${fila.objetivo}</textarea></td>
                <td><textarea class="form-control" name="modalidad_${index + 1}_planDiagnostico" style="height: 100px; min-width: 100px;" placeholder="">${fila.modalidad}</textarea></td>
                <td><textarea class="form-control" name="descripcion_${index + 1}_planDiagnostico" style="height: 100px; min-width: 100px;" placeholder="">${fila.descripcion}</textarea></td>
                <td><textarea class="form-control" name="dosis_${index + 1}_planDiagnostico" style="height: 100px; min-width: 100px;" placeholder="">${fila.dosis}</textarea></td>
            `;
            tableBody.appendChild(newRow);

            // Añadir evento de cambio a cada textarea para guardar los datos
            newRow.querySelectorAll('textarea').forEach(element => {
                element.addEventListener('change', guardarDatosDiagnostico1);
            });
        });
    }
}

// Cargar los datos al cargar la página
document.addEventListener('DOMContentLoaded', function () {
    cargarDatosDiagnostico();
});

// Evento para agregar filas dinámicamente y guardarlas
document.getElementById('agregarFilaBtn').addEventListener('click', function () {
    const tableBody = document.querySelector('#miembroPlanDiagnostico tbody');
    const newRow = document.createElement('tr');
    const rowIndex = tableBody.querySelectorAll('tr').length + 1;

    newRow.innerHTML = `
        <td><textarea class="form-control" name="objetivo_${rowIndex}_planDiagnostico" style="height: 100px; min-width: 100px;" placeholder=""></textarea></td>
        <td><textarea class="form-control" name="modalidad_${rowIndex}_planDiagnostico" style="height: 100px; min-width: 100px;" placeholder=""></textarea></td>
        <td><textarea class="form-control" name="descripcion_${rowIndex}_planDiagnostico" style="height: 100px; min-width: 100px;" placeholder=""></textarea></td>
        <td><textarea class="form-control" name="dosis_${rowIndex}_planDiagnostico" style="height: 100px; min-width: 100px;" placeholder=""></textarea></td>
    `;

    tableBody.appendChild(newRow);
    guardarDatosDiagnostico1();

    // Añadir eventos a los nuevos textarea
    newRow.querySelectorAll('textarea').forEach(element => {
        element.addEventListener('change', guardarDatosDiagnostico1);
    });
});

// --------------------------------------------------------------------------------------------

document.addEventListener("DOMContentLoaded", function () {

    function loadFormDataPlanDiagnostico() {
        const datosGuardados = JSON.parse(localStorage.getItem('datosDiagnostico')) || {};
        const { planTratamiento = [] } = datosGuardados;

        planTratamiento.forEach((item, index) => {
            const fila = document.querySelector(`#miembroPlanDiagnostico tbody tr:nth-child(${index + 1})`);
            if (fila) {
                fila.querySelector(`textarea[name="objetivo_${index + 1}_planDiagnostico"]`).value = item.objetivo || '';
                fila.querySelector(`textarea[name="modalidad_${index + 1}_planDiagnostico"]`).value = item.modalidad || '';
                fila.querySelector(`textarea[name="descripcion_${index + 1}_planDiagnostico"]`).value = item.descripcion || '';
                fila.querySelector(`textarea[name="dosis_${index + 1}_planDiagnostico"]`).value = item.dosis || '';
            }
        });
    }

    loadFormDataPlanDiagnostico();

    document.querySelectorAll('textarea').forEach(element => {
        element.addEventListener('input', guardarDatosDiagnostico1);
    });
});


// Obtener los botones por su ID
const botonVisible = document.getElementById('botonVisible');
const botonOculto = document.getElementById('botonOculto');
// Agregar un evento de clic al botón visible
botonVisible.addEventListener('click', function () {
    // Disparar el evento de clic del botón oculto
    botonOculto.click();
});
