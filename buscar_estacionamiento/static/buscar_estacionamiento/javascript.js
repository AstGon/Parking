document.addEventListener('DOMContentLoaded', function () {

    const selectHoraInicio = document.getElementById('hora_inicio');
    const selectHoraFin = document.getElementById('hora_fin');

    for (let hour = 0; hour <= 24; hour++) {
        const formattedHour = (hour < 10) ? `0${hour}:00` : `${hour}:00`;

        // Agrega opciones solo para las horas en los selectores de hora
        const optionInicio = document.createElement('option');
        optionInicio.value = formattedHour;
        optionInicio.textContent = formattedHour;
        selectHoraInicio.appendChild(optionInicio);

        const optionFin = document.createElement('option');
        optionFin.value = formattedHour;
        optionFin.textContent = formattedHour;
        selectHoraFin.appendChild(optionFin);
    }

    // Función para formatear las fechas en el formato deseado
    function formatFecha(fecha) {
        const options = {
            year: 'numeric',
            month: '2-digit',
            day: '2-digit'
        };
        return new Date(fecha).toLocaleDateString('es-CL', options);
    }

    // Obtén las fechas del formulario
    const fechaInicio = document.getElementById('fecha_inicio').value;
    const fechaFin = document.getElementById('fecha_fin').value;

    // Formatea las fechas y muesralas en el formulario
    document.getElementById('fecha_inicio').value = formatFecha(fechaInicio);
    document.getElementById('fecha_fin').value = formatFecha(fechaFin);

    function validateEmail() {
        var emailInput = document.getElementById('email');
        var emailValue = emailInput.value;
        var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,4}$/;


        if (!emailPattern.test(emailValue)) {
            alert('Correo electrónico no válido. Debe tener un formato válido.');
            emailInput.focus();
            return false;
        }

        // Aquí puedes realizar la verificación del dominio del lado del servidor
        // utilizando una solicitud AJAX para verificar la existencia del dominio.

        return true;
    }
    // Obtén todos los botones con la clase "btn-reservar"
    const buttons = document.querySelectorAll('.btn-reservar');

    // Agregar un controlador de eventos clic a cada botón
    buttons.forEach(function (button) {
        button.addEventListener('click', function () {
            // Obtiene el ID del modal desde el atributo "data-target"
            const modalId = button.getAttribute('data-target');
            const modal = document.querySelector(modalId);

            // Abre el modal cambiando la clase CSS
            modal.classList.add('show');
            modal.style.display = 'block';

            // Evita que el fondo sea desplazable mientras el modal esté abierto
            document.body.style.overflow = 'hidden';
        });
    });


});

// Obtén todos los botones con la clase "btn-reservar"
const buttons = document.querySelectorAll('.btn-reservar');

// Agregar un controlador de eventos clic a cada botón
buttons.forEach(function (button) {
    button.addEventListener('click', function () {
        // Obtiene el ID del modal desde el atributo "data-target"
        const modalId = button.getAttribute('data-target');
        const modal = document.querySelector(modalId);

        // Abre el modal cambiando la clase CSS
        modal.classList.add('show');
        modal.style.display = 'block';

        // Evita que el fondo sea desplazable mientras el modal esté abierto
        document.body.style.overflow = 'hidden';
    });
});

$(".btn-reservar").on("click", function () {
// Get the estacionamiento ID from the data attribute
var estacionamientoId = $(this).data("estacionamiento-id");

// Make an AJAX request to send the estacionamiento ID to your view
$.ajax({
    url: '/mostrar_estacionamiento/', // Reemplaza con la URL correcta de tu vista
    method: 'GET',
    data: {
        estacionamiento_id: estacionamientoId
    },
    success: function (data) {
        // Handle the response from the server here, if needed
    },
    error: function (error) {
        // Handle any errors here, if needed
    }
});
});
