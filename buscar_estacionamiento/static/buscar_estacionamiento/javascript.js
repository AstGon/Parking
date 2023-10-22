document.addEventListener('DOMContentLoaded', function () {

    const selectHoraInicio = document.getElementById('hora_inicio');
    const selectHoraFin = document.getElementById('hora_fin');
    
    for (let hour = 1; hour <= 24; hour++) {
        const formattedHour = (hour < 10) ? `0${hour}:00` : `${hour}:00`;
        
        const optionInicio = document.createElement('option');
        optionInicio.value = formattedHour;
        optionInicio.textContent = formattedHour;
        selectHoraInicio.appendChild(optionInicio);
    
        const optionFin = document.createElement('option');
        optionFin.value = formattedHour;
        optionFin.textContent = formattedHour;
        selectHoraFin.appendChild(optionFin);
    }
    
    
    // Espera a que el DOM esté completamente cargado

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

