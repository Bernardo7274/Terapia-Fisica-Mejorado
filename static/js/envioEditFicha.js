// Función para obtener el valor de un campo de texto
const obtenerValor = (id) =>
  document.getElementById(id)?.value || "No hay información";
const obtenerValorNumerico = (id) =>
  parseFloat(document.getElementById(id)?.value) || 0;
const obtenerValorEntero = (id) =>
  parseInt(document.getElementById(id)?.value, 10) || 0;

function guardarDatosFicha() {
  const datosFicha = {
    // Ficha identificaciones
    fechaElaboracion: obtenerValor("fecha"),
    folio: obtenerValor("folio"),
    nombrePaciente: obtenerValor("nombrePaciente"),
    sexo: obtenerValor("sexo"),
    fechaNacimiento: obtenerValor("fechaNacimiento"),
    edad: obtenerValor("edad"),
    lugarNacimiento: obtenerValor("lugarNacimiento"),
    estadoCivil: obtenerValor("civil"),
    ocupacion: obtenerValor("ocupacion"),
    nacionalidad: obtenerValor("nacionalidad"),
    domicilioActual: obtenerValor("domicilio"),
    telefono: obtenerValor("telefono"),
    nombreContactoEmergencia: obtenerValor("nombreContactoEmergencia"),
    telefonoEmergencia: obtenerValor("telefonoEmergencia"),
    diagnosticoMedico: obtenerValor("diagnosticoMedico"),
    elaboroHistorial: obtenerValor("elaboroHistorial"), // Verifica si esto es correcto
    motivoConsulta: obtenerValor("motivoConsulta"),
    // Antecedentes Personales No Patológicos
    PropiaRenta: obtenerValor("tipocasa"),
    Ventilacion: obtenerValor("ventilacion"),
    Iluminacion: obtenerValor("iluminacion"),
    Piso: obtenerValor("piso"),
    Electrodomesticos: obtenerValor("electrodomesticos"),
    Servicios: obtenerValor("Servicios"),
    DescripcionVivienda: obtenerValor("DescripcionVivienda"),
    NoComidasDia: obtenerValorEntero("comidasxdia"),
    AguaLts: obtenerValorNumerico("aguaLts"),
    GruposAlimenticios: obtenerValor("gruposAlimenticios"),
    DescripcionRutinaAlimenticia: obtenerValor("descripRutinaAlimentaria"),
    HigieneBucal: obtenerValor("higieneBucal"),
    BanosDia: obtenerValorEntero("bañosxdia"),
    CambiosRopa: obtenerValor("cambiosRopa"),
    ActividadFisica: obtenerValor("actFisica"),
    Deporte: obtenerValor("deporte"),
    Ocio: obtenerValor("ocio"),
    Ocupacion1: obtenerValor("ocupacion1"),
    // Antecedentes Heredofamiliares
    antecedentes: [
      "Cáncer",
      "Diabetes",
      "Hipertensión",
      "Enfermedades Cardiacas",
      "Enfermedades Mentales",
      "Alergias",
    ].map((enfermedad) => ({
      enfermedad,
      si: document.querySelector(`input[name="${enfermedad}_si"]`)?.checked
        ? 1
        : 0,
      no: document.querySelector(`input[name="${enfermedad}_no"]`)?.checked
        ? 1
        : 0,
      parentesco:
        document.querySelector(`input[name="${enfermedad}_parentesco"]`)
          ?.value || "No hay información",
      vivo: document.querySelector(`input[name="${enfermedad}_vivo"]`)?.checked
        ? 1
        : 0,
      muerto: document.querySelector(`input[name="${enfermedad}_muerto"]`)
        ?.checked
        ? 1
        : 0,
      otro: obtenerValor("otros"),
      observaciones: obtenerValor("observaciones"),
    })),
    // Antecedentes Personales Patológicos
    datosPatologicos: [
      "Traumatismos",
      "Cirugías",
      "Luxaciones",
      "Alergias",
      "Toxicomanías",
      "Padecimientos psiquiátricos",
    ].map((patologia) => ({
      patologia,
      si_pa: document.querySelector(`input[name="${patologia}_si"]`)?.checked
        ? 1
        : 0,
      no_pa: document.querySelector(`input[name="${patologia}_no"]`)?.checked
        ? 1
        : 0,
      edad_presento:
        document.querySelector(`input[name="${patologia}_edad"]`)?.value ||
        "No hay información",
      secuela:
        document.querySelector(`input[name="${patologia}_secuelas"]`)?.value ||
        "No hay información",
      inmunizaciones: obtenerValor("inmunizaciones"),
      observaciones1: obtenerValor("observaciones_ante"),
    })),
    // Antecedentes Ginecobstétricos
    menarquia: obtenerValor("menarquia"),
    fecha_ultima_menstruacion: obtenerValor("ultimaMenstruacion"),
    caracteristicas_menstruacion: obtenerValor("caracteristicasMenstruacion"),
    inicio_vida_sexual: obtenerValor("inicioVidaSexual"),
    uso_anticonceptivos: obtenerValor("usoAnticonceptivos"),
    numero_embarazos: obtenerValor("numEmbarazos"),
    numero_partos: obtenerValor("numPartos"),
    numero_cesareas: obtenerValor("numCesareas"),
    observaciones_gine: obtenerValor("observacionesGine"),
    // Antecedentes De Padecimiento Actual
    ac_descripcion: obtenerValor("describe"),
    // Exploracion
    habitus_exterior: obtenerValor("habitusExte"),
    peso: obtenerValor("peso"),
    altura: obtenerValor("talla"),
    imc: obtenerValor("tensionArterial"),
    temperatura: obtenerValor("temperatura"),
    pulso_cardiaco: obtenerValor("frecuenciaCardiaca"),
    frecuencia_respiratoria: obtenerValor("frecuenciaRespiratoria"),
    presion_arterial: obtenerValorEntero("saturacion_de_oxígeno"),
    saturacion_oxigeno: obtenerValorNumerico("presionArterial"),
    observaciones2: obtenerValor("observacionesexplofisica"),
    resultados_previos_actuales: obtenerValor("resultadospreviosyactuales"),
  };
  localStorage.setItem("datosFicha", JSON.stringify(datosFicha));
}

document
  .getElementById("fichaForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    guardarDatosFicha();
    window.location.href = "/EdicionMiembroSuperior"; // Redirige a la siguiente página
  });

document.querySelectorAll("input, select, textarea").forEach((element) => {
  element.addEventListener("change", guardarDatosFicha);
});

// Obtener los botones por su ID
const botonVisible = document.getElementById("botonVisible");
const botonOculto = document.getElementById("botonOculto");
// Agregar un evento de clic al botón visible
botonVisible.addEventListener("click", function () {
  // Disparar el evento de clic del botón oculto
  botonOculto.click();
});

// ----------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function () {
  // Función para guardar los datos del formulario en localStorage
  function saveFormData() {
    const formData = {};
    const inputs = document.querySelectorAll(
      "#fichaForm input, #fichaForm select"
    );
    inputs.forEach((input) => {
      formData[input.id] = input.value;
    });
    localStorage.setItem("fichaFormData", JSON.stringify(formData));
  }

  // Función para cargar los datos del formulario desde localStorage
  function loadFormData() {
    const formData = JSON.parse(localStorage.getItem("fichaFormData"));
    if (formData) {
      const inputs = document.querySelectorAll(
        "#fichaForm input, #fichaForm select"
      );
      inputs.forEach((input) => {
        if (formData[input.id]) {
          input.value = formData[input.id];
        }
      });
    }
  }

  // Función para guardar los datos del primer formulario en localStorage
  function saveFormData1() {
    const formData1 = {};
    const inputs1 = document.querySelectorAll(
      "#fichaForm1 input, #fichaForm1 textarea"
    );
    inputs1.forEach((input) => {
      formData1[input.id] = input.value;
    });
    localStorage.setItem("fichaFormData1", JSON.stringify(formData1));
  }

  // Función para cargar los datos del primer formulario desde localStorage
  function loadFormData1() {
    const formData1 = JSON.parse(localStorage.getItem("fichaFormData1"));
    if (formData1) {
      const inputs1 = document.querySelectorAll(
        "#fichaForm1 input, #fichaForm1 textarea"
      );
      inputs1.forEach((input) => {
        if (formData1[input.id]) {
          input.value = formData1[input.id];
        }
      });
    }
  }

  // Función para guardar los datos del segundo formulario en localStorage
  function saveFormData2() {
    const formData2 = {};
    const inputs2 = document.querySelectorAll("#fichaForm2 input");
    inputs2.forEach((input) => {
      if (input.type === "checkbox") {
        formData2[input.id] = input.checked;
      } else {
        formData2[input.id] = input.value;
      }
    });
    localStorage.setItem("fichaFormData2", JSON.stringify(formData2));
  }

  // Función para cargar los datos del segundo formulario desde localStorage
  function loadFormData2() {
    const formData2 = JSON.parse(localStorage.getItem("fichaFormData2"));
    if (formData2) {
      const inputs2 = document.querySelectorAll("#fichaForm2 input");
      inputs2.forEach((input) => {
        if (input.type === "checkbox") {
          input.checked = formData2[input.id];
        } else {
          input.value = formData2[input.id];
        }
      });
    }
  }

  // Función para guardar los datos del tercer formulario en localStorage
  function saveFormData3() {
    const formData3 = {};
    const inputs3 = document.querySelectorAll("#fichaForm3 input");
    inputs3.forEach((input) => {
      if (input.type === "checkbox") {
        formData3[input.id] = input.checked;
      } else {
        formData3[input.id] = input.value;
      }
    });
    localStorage.setItem("fichaFormData3", JSON.stringify(formData3));
  }

  // Función para cargar los datos del tercer formulario desde localStorage
  function loadFormData3() {
    const formData3 = JSON.parse(localStorage.getItem("fichaFormData3"));
    if (formData3) {
      const inputs3 = document.querySelectorAll("#fichaForm3 input");
      inputs3.forEach((input) => {
        if (input.type === "checkbox") {
          input.checked = formData3[input.id];
        } else {
          input.value = formData3[input.id];
        }
      });
    }
  }

  // Función para guardar los datos del cuarto formulario en localStorage
  function saveFormData4() {
    const formData4 = {};
    const inputs4 = document.querySelectorAll("#fichaForm4 input");
    inputs4.forEach((input) => {
      formData4[input.id] = input.value;
    });
    localStorage.setItem("fichaFormData4", JSON.stringify(formData4));
  }

  // Función para cargar los datos del cuarto formulario desde localStorage
  function loadFormData4() {
    const formData4 = JSON.parse(localStorage.getItem("fichaFormData4"));
    if (formData4) {
      const inputs4 = document.querySelectorAll("#fichaForm4 input");
      inputs4.forEach((input) => {
        if (formData4[input.id]) {
          input.value = formData4[input.id];
        }
      });
    }
  }

  // Función para guardar los datos del quinto formulario en localStorage
  function saveFormData5() {
    const formData5 = {};
    const inputs5 = document.querySelectorAll("#fichaForm5 textarea");
    inputs5.forEach((input) => {
      formData5[input.id] = input.value;
    });
    localStorage.setItem("fichaFormData5", JSON.stringify(formData5));
  }

  // Función para cargar los datos del quinto formulario desde localStorage
  function loadFormData5() {
    const formData5 = JSON.parse(localStorage.getItem("fichaFormData5"));
    if (formData5) {
      const inputs5 = document.querySelectorAll("#fichaForm5 textarea");
      inputs5.forEach((input) => {
        if (formData5[input.id]) {
          input.value = formData5[input.id];
        }
      });
    }
  }

  // Función para guardar los datos del sexto formulario en localStorage
  function saveFormData6() {
    const formData6 = {};
    const inputs6 = document.querySelectorAll(
      "#fichaForm6 input, #fichaForm6 textarea"
    );
    inputs6.forEach((input) => {
      formData6[input.id] = input.value;
    });
    localStorage.setItem("fichaFormData6", JSON.stringify(formData6));
  }

  // Función para cargar los datos del sexto formulario desde localStorage
  function loadFormData6() {
    const formData6 = JSON.parse(localStorage.getItem("fichaFormData6"));
    if (formData6) {
      const inputs6 = document.querySelectorAll(
        "#fichaForm6 input, #fichaForm6 textarea"
      );
      inputs6.forEach((input) => {
        if (formData6[input.id]) {
          input.value = formData6[input.id];
        }
      });
    }
  }

  // Cargar datos al cargar la página
  loadFormData();
  loadFormData1();
  loadFormData2();
  loadFormData3();
  loadFormData4();
  loadFormData5();
  loadFormData6();

  // Guardar datos en tiempo real
  const inputs = document.querySelectorAll(
    "#fichaForm input, #fichaForm select"
  );
  inputs.forEach((input) => {
    input.addEventListener("input", saveFormData);
  });

  // Guardar datos en tiempo real para el primer formulario
  const inputs1 = document.querySelectorAll(
    "#fichaForm1 input, #fichaForm1 textarea"
  );
  inputs1.forEach((input) => {
    input.addEventListener("input", saveFormData1);
  });

  // Guardar datos en tiempo real para el segundo formulario
  const inputs2 = document.querySelectorAll("#fichaForm2 input");
  inputs2.forEach((input) => {
    input.addEventListener("input", saveFormData2);
    if (input.type === "checkbox") {
      input.addEventListener("change", saveFormData2);
    }
  });

  // Guardar datos en tiempo real para el tercer formulario
  const inputs3 = document.querySelectorAll("#fichaForm3 input");
  inputs3.forEach((input) => {
    input.addEventListener("input", saveFormData3);
    if (input.type === "checkbox") {
      input.addEventListener("change", saveFormData3);
    }
  });

  // Guardar datos en tiempo real para el cuarto formulario
  const inputs4 = document.querySelectorAll("#fichaForm4 input");
  inputs4.forEach((input) => {
    input.addEventListener("input", saveFormData4);
  });

  // Guardar datos en tiempo real para el quinto formulario
  const inputs5 = document.querySelectorAll("#fichaForm5 textarea");
  inputs5.forEach((input) => {
    input.addEventListener("input", saveFormData5);
  });

  // Guardar datos en tiempo real para el sexto formulario
  const inputs6 = document.querySelectorAll(
    "#fichaForm6 input, #fichaForm6 textarea"
  );
  inputs6.forEach((input) => {
    input.addEventListener("input", saveFormData6);
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const fechaElaboracion = document.getElementById("fecha");
  const today = new Date();
  const year = today.getFullYear();
  const month = String(today.getMonth() + 1).padStart(2, "0"); // Los meses van de 0 a 11, por eso sumamos 1
  const day = String(today.getDate()).padStart(2, "0"); // Asegura que siempre tenga dos dígitos
  const localDate = `${year}-${month}-${day}`;
  fechaElaboracion.value = localDate; // Asigna la fecha en formato local
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
  fetch("/consultar", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ id: id }),
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

      // Datos de ficha_identificaciones
      establecerValor(
        "fecha",
        formatearFechaParaInputDate(data.fecha_elaboracion)
      );
      establecerValor("folio", data.folio);
      establecerValor("nombrePaciente", data.nombre_paciente);
      establecerValor("sexo", data.genero);
      establecerValor(
        "fechaNacimiento",
        formatearFechaParaInputDate(data.fecha_nacimiento)
      );
      establecerValor("edad", data.edad);
      establecerValor("lugarNacimiento", data.lugar_nacimiento);
      establecerValor("civil", data.estado_civil);
      establecerValor("ocupacion", data.ocupacion);
      establecerValor("nacionalidad", data.nacionalidad);
      establecerValor("domicilio", data.domicilio_actual);
      establecerValor("telefono", data.telefono);
      establecerValor(
        "nombreContactoEmergencia",
        data.contacto_emergencia_nombre
      );
      establecerValor("telefonoEmergencia", data.contacto_emergencia_telefono);
      establecerValor("diagnosticoMedico", data.diagnostico_medico);
      establecerValor("elaboroHistorial", data.elaboro_historial_clinico);
      establecerValor("motivoConsulta", data.motivo_consulta);

      // Datos de antecedentespersonalesnopatologicos
      establecerValor("tipocasa", data.PropiaRenta);
      establecerValor("ventilacion", data.Ventilacion);
      establecerValor("iluminacion", data.Iluminacion);
      establecerValor("piso", data.Piso);
      establecerValor("electrodomesticos", data.Electrodomesticos);
      establecerValor("Servicios", data.Servicios);
      establecerValor("DescripcionVivienda", data.DescripcionVivienda);
      establecerValor("comidasxdia", data.NoComidasDia);
      establecerValor("aguaLts", data.AguaLts);
      establecerValor("gruposAlimenticios", data.GruposAlimenticios);
      establecerValor(
        "descripRutinaAlimentaria",
        data.DescripcionRutinaAlimenticia
      );
      establecerValor("higieneBucal", data.HigieneBucal);
      establecerValor("bañosxdia", data.BanosDia);
      establecerValor("cambiosRopa", data.CambiosRopa);
      establecerValor("actFisica", data.ActividadFisica);
      establecerValor("deporte", data.Deporte);
      establecerValor("ocio", data.Ocio);
      establecerValor("ocupacion1", data.Ocupacion);
    })
    .catch((error) => {
      console.error("Error al consultar los datos:", error);
    });
} else {
  console.error("No se encontró un ID en el localStorage");
}



































































if (id) {
  fetch("/consultarAntecedentesHeredoFamiliares", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ id: id }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        console.error("Error desde el servidor:", data.error);
        return;
      }

      console.log("Datos recibidos:", data);

      // Actualizar los campos del DOM con los datos obtenidos
      data.forEach((antecedente) => {
        const {
          enfermedad,
          si,
          no,
          parentesco,
          vivo,
          muerto,
          otro,
          observaciones,
        } = antecedente;

        // Actualizar valores de los checkboxes
        establecerValor(`${enfermedad}_si`, si);
        establecerValor(`${enfermedad}_no`, no);
        establecerValor(`${enfermedad}_vivo`, vivo);
        establecerValor(`${enfermedad}_muerto`, muerto);

        // Actualizar valores de los campos de texto
        establecerValor(`${enfermedad}_parentesco`, parentesco);
        establecerValor("otros", otro);
        establecerValor("observaciones", observaciones);
      });
    })
    .catch((error) => {
      console.error("Error al consultar los datos:", error);
    });
} else {
  console.error("No se encontró un ID en el localStorage");
}

if (id) {
  fetch("/consultarAntecedentesPatologicos", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ id: id }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        console.error("Error desde el servidor:", data.error);
        return;
      }

      console.log("Datos recibidos:", data);

      // Actualizar los campos en el DOM con los datos obtenidos
      data.forEach((patologia) => {
        const {
          patologia: nombrePatologia,
          si,
          no,
          edad_presentacion,
          secuelas_complicaciones,
          inmunizaciones,
          observaciones,
        } = patologia;

        // Actualizar valores de los checkboxes
        establecerValor(`${nombrePatologia}_si`, si);
        establecerValor(`${nombrePatologia}_no`, no);

        // Actualizar valores de los campos de texto
        establecerValor(`${nombrePatologia}_edad`, edad_presentacion);
        establecerValor(`${nombrePatologia}_secuelas`, secuelas_complicaciones);
        establecerValor("inmunizaciones", inmunizaciones);
        establecerValor("observaciones_ante", observaciones);
      });
    })
    .catch((error) => {
      console.error("Error al consultar los datos:", error);
    });
} else {
  console.error("No se encontró un ID en el localStorage");
}

if (id) {
  fetch("/consultarAntecedentesGinecobstetricos", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ id: id }),
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

      // Actualizar los campos en el DOM con los datos obtenidos
      establecerValor("menarquia", data.menarquia);
      establecerValor("ultimaMenstruacion", formatearFechaParaInputDate(data.fecha_ultima_menstruacion));
      establecerValor(
        "caracteristicasMenstruacion",
        data.caracteristicas_menstruacion
      );
      establecerValor("inicioVidaSexual", formatearFechaParaInputDate(data.inicio_vida_sexual));
      establecerValor("usoAnticonceptivos", data.uso_anticonceptivos);
      establecerValor("numEmbarazos", data.numero_embarazos);
      establecerValor("numPartos", data.numero_partos);
      establecerValor("numCesareas", data.numero_cesareas);
      establecerValor("observacionesGine", data.observaciones);
    })
    .catch((error) => {
      console.error("Error al consultar los datos:", error);
    });
} else {
  console.error("No se encontró un ID en el localStorage");
}

if (id) {
  fetch("/consultarPadecimientoActual", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ id: id }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        console.error("Error desde el servidor:", data.error);
        return;
      }

      console.log("Datos recibidos:", data);

      // Actualizar el campo en el DOM con los datos obtenidos
      establecerValor("describe", data.descripcion);
    })
    .catch((error) => {
      console.error("Error al consultar los datos:", error);
    });
} else {
  console.error("No se encontró un ID en el localStorage");
}

if (id) {
  fetch("/consultarExploracion", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ id: id }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        console.error("Error desde el servidor:", data.error);
        return;
      }

      console.log("Datos recibidos:", data);

      // Actualizar los campos en el DOM con los datos obtenidos
      establecerValor("habitusExte", data.habitus_exterior);
      establecerValor("peso", data.peso);
      establecerValor("talla", data.altura);
      establecerValor("tensionArterial", data.imc);
      establecerValor("temperatura", data.temperatura);
      establecerValor("frecuenciaCardiaca", data.pulso_cardiaco);
      establecerValor("frecuenciaRespiratoria", data.frecuencia_respiratoria);
      establecerValor("presionArterial", data.presion_arterial);
      establecerValor("saturacion_de_oxígeno", data.saturacion_oxigeno);
      establecerValor("observacionesexplofisica", data.observaciones);
      establecerValor(
        "resultadospreviosyactuales",
        data.resultados_previos_actuales
      );
    })
    .catch((error) => {
      console.error("Error al consultar los datos:", error);
    });
} else {
  console.error("No se encontró un ID en el localStorage");
}
