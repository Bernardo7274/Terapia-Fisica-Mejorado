document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.card-header').forEach(function (header) {
        header.addEventListener('click', function () {
            let icon = header.querySelector('i');
            let isCollapsed = header.getAttribute('aria-expanded') === 'true';
            icon.classList.toggle('fa-chevron-up', !isCollapsed);
            icon.classList.toggle('fa-chevron-down', isCollapsed);
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.card-header').forEach(function (header) {
        header.addEventListener('click', function () {
            let icon = header.querySelector('i');
            let isCollapsed = header.getAttribute('aria-expanded') === 'true';
            icon.classList.toggle('fa-chevron-up', !isCollapsed);
            icon.classList.toggle('fa-chevron-down', isCollapsed);
        });
    });
});

function eliminarContenedor1() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha1');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}



function eliminarContenedor2() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha2');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor3() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha3');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor4() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha4');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor5() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha5');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor6() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha6');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor7() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha7');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor8() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha8');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor9() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha9');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor10() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha10');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor10() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha10');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor11() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha11');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor12() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha12');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor13() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha13');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor14() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha14');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor15() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha15');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor16() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha16');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor17() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha17');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor18() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha18');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor19() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha19');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor20() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha20');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor21() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha21');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor22() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha22');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor23() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha23');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor24() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha24');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}

function eliminarContenedor25() {
    var confirmar = confirm("¿Estás seguro de que deseas eliminar este contenedor?");
    if (confirmar) {
        var contenedor = document.getElementById('contenedorFicha25');
        var inputs = contenedor.getElementsByTagName('input');
        var selects = contenedor.getElementsByTagName('select');
        var textareas = contenedor.getElementsByTagName('textarea');
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.type === 'checkbox' || input.type === 'radio') {
                input.checked = false;
            } else {
                input.value = '';
            }
        }
        for (var i = 0; i < selects.length; i++) {
            selects[i].selectedIndex = -1;
        }
        for (var i = 0; i < textareas.length; i++) {
            textareas[i].value = '';
        }
        contenedor.parentNode.removeChild(contenedor);
    }
}