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
    window.location.href = "/MiembroSuperior"; // Redirige a la siguiente página
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
  function generarFolioAleatorio() {
    const fecha = new Date();
    const año = fecha.getFullYear().toString().slice(-2); // Últimos 2 dígitos del año
    const dia = fecha.getDate().toString().padStart(2, "0"); // Día en formato DD
    const numeroAleatorio = Math.floor(1000 + Math.random() * 9999).toString(); // Número aleatorio de 2 dígitos

    return año + dia + numeroAleatorio; // Genera un folio de 6 dígitos
  }

  function asignarFolio() {
    const folio = generarFolioAleatorio();
    document.getElementById("folio").value = folio;
  }

  asignarFolio();
});

// ------------------------------------------------------------------------------
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
