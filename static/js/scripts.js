// Obtener el formulario y el botón de envío
const submitButton = document.getElementById('submitButton');

// Escuchar el evento de envío del formulario
document.getElementById('contactForm').addEventListener('submit', function(e) {
    // Cambiar el texto del botón y el color
    submitButton.textContent = "Enviado";
    submitButton.classList.add('sent');  // Agregar clase para cambiar el color a verde

    // Esperar 2 segundos antes de restaurar el botón a su estado original
    setTimeout(function() {
        submitButton.textContent = "Enviar";  // Restaurar el texto original
        submitButton.classList.remove('sent');  // Eliminar la clase para volver al color original
    }, 2000);
    
    // Permitir que el formulario se envíe después de los cambios visuales
});

const flashMessage = document.getElementById('flashMessage');

if (flashMessage) {
    // Mostrar el mensaje flash
    flashMessage.classList.add('show');

    // Ocultar el mensaje flash después de 3 segundos
    setTimeout(() => {
        flashMessage.classList.remove('show');
    }, 1000);
}
