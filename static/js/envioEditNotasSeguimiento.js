const obtenerValor = (id) => document.getElementById(id)?.value || "";
const obtenerValorNumerico = (id) =>
  parseFloat(document.getElementById(id)?.value) || 0;
const obtenerValorEntero = (id) =>
  parseInt(document.getElementById(id)?.value, 10) || 0;

function guardarDatosNotasSeguimiento() {
  const datosPrincipal = {
    nombrePaciente_Seguimiento: obtenerValor("nombrePaciente_notasSeguimiento"),
    diagnostico_Seguimiento: obtenerValor("diagnostico_notasSeguimiento"),
    folio_Seguimiento: obtenerValor("folio_notasSeguimiento"),
    fecha_Seguimiento: obtenerValor("fecha_notasSeguimiento"),
    sesion_Seguimiento: obtenerValor("sesion_notasSeguimiento"),
    notas_Seguimiento: obtenerValor("notas_notasSeguimiento"),
    sugerencias_Seguimiento: obtenerValor("sugerencias_notasSeguimiento"),
    nombrefirma_Seguimiento: obtenerValor("nombrefirma_notasSeguimiento"),
  };

  const secciones = document.querySelectorAll("#contenedorSecciones .card");
  const datosTodasSecciones = [];

  secciones.forEach((seccion, index) => {
    const datosNotasSeguimiento = {
      nombrePaciente_Seguimiento: obtenerValor(
        `nombrePaciente_notasSeguimiento_${index}`
      ),
      diagnostico_Seguimiento: obtenerValor(
        `diagnostico_notasSeguimiento_${index}`
      ),
      folio_Seguimiento: obtenerValor(`folio_notasSeguimiento_${index}`),
      fecha_Seguimiento: obtenerValor(`fecha_notasSeguimiento_${index}`),
      sesion_Seguimiento: obtenerValor(`sesion_notasSeguimiento_${index}`),
      notas_Seguimiento: obtenerValor(`notas_notasSeguimiento_${index}`),
      sugerencias_Seguimiento: obtenerValor(
        `sugerencias_notasSeguimiento_${index}`
      ),
      nombrefirma_Seguimiento: obtenerValor(
        `nombrefirma_notasSeguimiento_${index}`
      ),
    };
    datosTodasSecciones.push(datosNotasSeguimiento);
  });

  const datosCompletos = {
    principal: datosPrincipal,
    secciones: datosTodasSecciones,
  };

  localStorage.setItem("datosNotasSeguimiento", JSON.stringify(datosCompletos));
}

function generarFolio() {
  const fecha = new Date();
  const año = fecha.getFullYear().toString().slice(-2); // Dos últimos dígitos del año
  const dia = fecha.getDate().toString().padStart(2, "0"); // Día en formato de dos dígitos
  const aleatorio = Math.floor(Math.random() * 100)
    .toString()
    .padStart(2, "0"); // Número aleatorio entre 00 y 99
  return año + dia + aleatorio;
}

function mostrarFolioEnCampos() {
  // Mostrar folio en todas las secciones agregadas dinámicamente
  const secciones = document.querySelectorAll("#contenedorSecciones .card");
  secciones.forEach((seccion, index) => {
    const folioSeccion = generarFolio();
    document.getElementById(`folio_notasSeguimiento_${index}`).value =
      folioSeccion;
  });
}

document
  .getElementById("miembroNotasSeguimiento")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    guardarDatosNotasSeguimiento();
    window.location.href = "/EdicionPlanDiagnostico";
  });

document.querySelectorAll("input, select, textarea").forEach((element) => {
  element.addEventListener("change", guardarDatosNotasSeguimiento);
});

// Función para formatear fechas en formato YYYY-MM-DD
function formatearFechaParaInputDate(fecha) {
  if (!fecha) return ""; // Manejar valores nulos o indefinidos
  const fechaObj = new Date(fecha);
  const anio = fechaObj.getFullYear();
  const mes = String(fechaObj.getMonth() + 1).padStart(2, "0");
  const dia = String(fechaObj.getDate()).padStart(2, "0");
  return `${anio}-${mes}-${dia}`;
}

function agregarSeccion(datos = {}) {
  const contenedorSecciones = document.getElementById("contenedorSecciones");
  const numSecciones = contenedorSecciones.children.length;
  const nuevaSeccion = document.createElement("div");
  nuevaSeccion.id = `contenedorFicha_${numSecciones}`;
  nuevaSeccion.className = "card mb-3";
  nuevaSeccion.innerHTML = `
          <div class="card-header" data-toggle="collapse" data-target="#notasSeguimiento_${numSecciones}" aria-expanded="true" aria-controls="notasSeguimiento_${numSecciones}">
              Notas de seguimiento
              <i class="fas fa-chevron-up float-right"></i>
              <button type="button" class="btn btn-danger btn-sm float-right mr-2" onclick="eliminarSeccion(${numSecciones})">Eliminar sección</button>
          </div>
          <div id="notasSeguimiento_${numSecciones}" class="collapse show">
              <div class="card-body">
                  <form class="row g-3 needs-validation" novalidate id="miembroNotasSeguimiento_${numSecciones}">
                      <div class="form-group col-md-12 mt-1">
                          <label for="nombrePaciente_${numSecciones}" class="form-label">Nombre del Paciente:</label>
                          <input type="text" class="form-control" id="nombrePaciente_notasSeguimiento_${numSecciones}" required value="${
    datos.nombre || ""
  }">
                      </div>
                      <div class="form-group col-md-6 mt-1">
                          <label for="diagnostico_${numSecciones}" class="form-label">Diagnóstico:</label>
                          <input type="text" class="form-control" id="diagnostico_notasSeguimiento_${numSecciones}" required value="${
    datos.diagnostico || ""
  }">
                      </div>
                      <div class="form-group col-md-4 mt-1">
                          <label for="folio_${numSecciones}" class="form-label">Folio:</label>
                          <input type="text" class="form-control" id="folio_notasSeguimiento_${numSecciones}" required readonly value="${
    datos.folio || ""
  }">
                      </div>
                      <div class="form-group col-md-8 mt-1">
                          <label for="fecha_${numSecciones}">Fecha:</label>
                          <input type="date" class="form-control" id="fecha_notasSeguimiento_${numSecciones}" name="fecha" value="${
    formatearFechaParaInputDate(datos.fecha) || ""
  }">
                      </div>
                      <div class="form-group col-md-4 mt-1">
                          <label for="sesion_${numSecciones}" class="form-label">No. de sesión:</label>
                          <input type="text" class="form-control" id="sesion_notasSeguimiento_${numSecciones}" required value="${
    datos.numero_sesion || ""
  }">
                      </div>
                      <div class="form-group col-md-12 mt-1">
                          <label for="notas_${numSecciones}">Notas:</label>
                          <textarea class="form-control" id="notas_notasSeguimiento_${numSecciones}" style="height: 100px">${
    datos.notas || ""
  }</textarea>
                      </div>
                      <div class="form-group col-md-12 mt-1">
                          <label for="sugerencias_${numSecciones}">Sugerencias/observaciones:</label>
                          <textarea class="form-control" id="sugerencias_notasSeguimiento_${numSecciones}" style="height: 100px">${
    datos.sugerencias_observaciones || ""
  }</textarea>
                      </div>
                      <div class="form-group col-md-12 mt-1">
                          <label for="nombrefirma_${numSecciones}">Nombre y firma del tratante:</label>
                          <textarea class="form-control" id="nombrefirma_notasSeguimiento_${numSecciones}" style="height: 100px">${
    datos.nombreYfirma_tratante || ""
  }</textarea>
                      </div>
                  </form>
              </div>
          </div>
      `;
  contenedorSecciones.appendChild(nuevaSeccion);

  //   const folioSeccion = generarFolio();
  //   document.getElementById(`folio_notasSeguimiento_${numSecciones}`).value =
  //     folioSeccion;

  const nuevaSeccionInputs = nuevaSeccion.querySelectorAll("input, textarea");
  nuevaSeccionInputs.forEach((input) => {
    input.addEventListener("change", guardarDatosNotasSeguimiento);
  });

  guardarDatosNotasSeguimiento();
}

function eliminarSeccion(numSecciones) {
  const seccion = document.getElementById(`contenedorFicha_${numSecciones}`);
  if (seccion) {
    seccion.remove();
    guardarDatosNotasSeguimiento();
  }
}

function loadFormData() {
  let datosGuardados;
  try {
    datosGuardados = JSON.parse(
      localStorage.getItem("datosNotasSeguimiento")
    ) || { principal: {}, secciones: [] };
  } catch (error) {
    console.error("Error al cargar datos del localStorage:", error);
    datosGuardados = { principal: {}, secciones: [] };
  }

  if (datosGuardados.principal) {
    document.getElementById("nombrePaciente_notasSeguimiento").value =
      datosGuardados.principal.nombrePaciente_Seguimiento || "";
    document.getElementById("diagnostico_notasSeguimiento").value =
      datosGuardados.principal.diagnostico_Seguimiento || "";
    document.getElementById("folio_notasSeguimiento").value =
      datosGuardados.principal.folio_Seguimiento || "";
    document.getElementById("fecha_notasSeguimiento").value =
      datosGuardados.principal.fecha_Seguimiento || "";
    document.getElementById("sesion_notasSeguimiento").value =
      datosGuardados.principal.sesion_Seguimiento || "";
    document.getElementById("notas_notasSeguimiento").value =
      datosGuardados.principal.notas_Seguimiento || "";
    document.getElementById("sugerencias_notasSeguimiento").value =
      datosGuardados.principal.sugerencias_Seguimiento || "";
    document.getElementById("nombrefirma_notasSeguimiento").value =
      datosGuardados.principal.nombrefirma_Seguimiento || "";
  }

  if (Array.isArray(datosGuardados.secciones)) {
    datosGuardados.secciones.forEach((seccion, index) => {
      agregarSeccion();
      document.getElementById(
        `nombrePaciente_notasSeguimiento_${index}`
      ).value = seccion.nombrePaciente_Seguimiento || "";
      document.getElementById(`diagnostico_notasSeguimiento_${index}`).value =
        seccion.diagnostico_Seguimiento || "";
      document.getElementById(`folio_notasSeguimiento_${index}`).value =
        seccion.folio_Seguimiento || generarFolio();
      document.getElementById(`fecha_notasSeguimiento_${index}`).value =
        seccion.fecha_Seguimiento || "";
      document.getElementById(`sesion_notasSeguimiento_${index}`).value =
        seccion.sesion_Seguimiento || "";
      document.getElementById(`notas_notasSeguimiento_${index}`).value =
        seccion.notas_Seguimiento || "";
      document.getElementById(`sugerencias_notasSeguimiento_${index}`).value =
        seccion.sugerencias_Seguimiento || "";
      document.getElementById(`nombrefirma_notasSeguimiento_${index}`).value =
        seccion.nombrefirma_Seguimiento || "";
    });
  }
}

window.onload = function () {
  mostrarFolioEnCampos();
  loadFormData();
};

document
  .getElementById("agregarSeccion")
  .addEventListener("click", agregarSeccion);

const botonVisible = document.getElementById("botonVisible");
const botonOculto = document.getElementById("botonOculto");
botonVisible.addEventListener("click", function () {
  botonOculto.click();
});

// Obtener el ID del localStorage
const id = localStorage.getItem("Id");
console.log("El Id almacenado es:", id);
if (!id) {
  console.error("No se encontró un ID en el localStorage");
} else {
  fetch("/consultar_notas", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ id: localStorage.getItem("Id") }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        console.error("Error desde el servidor:", data.error);
        return;
      }

      console.log("Datos recibidos:", data);

      // Función para formatear fechas en formato YYYY-MM-DD
      function formatearFechaParaInputDate(fecha) {
        if (!fecha) return ""; // Manejar valores nulos o indefinidos
        const fechaObj = new Date(fecha);
        const anio = fechaObj.getFullYear();
        const mes = String(fechaObj.getMonth() + 1).padStart(2, "0");
        const dia = String(fechaObj.getDate()).padStart(2, "0");
        return `${anio}-${mes}-${dia}`;
      }

      if (data.datos && data.datos.length > 0) {
        // Primer registro se asigna a datosPrincipal
        const primerRegistro = data.datos[0];
        document.getElementById("nombrePaciente_notasSeguimiento").value =
          primerRegistro.nombre || "";
        document.getElementById("diagnostico_notasSeguimiento").value =
          primerRegistro.diagnostico || "";
        document.getElementById("folio_notasSeguimiento").value =
          primerRegistro.folio || "";
        document.getElementById("fecha_notasSeguimiento").value =
          formatearFechaParaInputDate(primerRegistro.fecha) || "";
        document.getElementById("sesion_notasSeguimiento").value =
          primerRegistro.numero_sesion || "";
        document.getElementById("notas_notasSeguimiento").value =
          primerRegistro.notas || "";
        document.getElementById("sugerencias_notasSeguimiento").value =
          primerRegistro.sugerencias_observaciones || "";
        document.getElementById("nombrefirma_notasSeguimiento").value =
          primerRegistro.nombreYfirma_tratante || "";

        // Agregar los registros restantes como nuevas secciones
        const registrosRestantes = data.datos.slice(1);
        registrosRestantes.forEach((registro) => {
          agregarSeccion(registro);
        });
      }
    })
    .catch((error) => {
      console.error("Error al consultar los datos:", error);
    });
}
