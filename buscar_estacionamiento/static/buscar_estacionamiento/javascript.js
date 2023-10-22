
document.addEventListener('DOMContentLoaded', function () {
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

$(document).ready(function () {
    $(".btn-reservar").on("click", function () {
        // Get the estacionamiento ID from the data attribute
        var estacionamientoId = $(this).data("estacionamiento-id");

        // Make an AJAX request to send the estacionamiento ID to your view
        $.ajax({
            url: '/mostrar_estacionamiento/',  // Reemplaza con la URL correcta de tu vista
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
});
