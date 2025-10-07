document.addEventListener('DOMContentLoaded', () => {
    const deleteForms = document.querySelectorAll('form button[type="submit"].btn-danger');
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    let currentForm = null;

    const dontAsk = localStorage.getItem('dontAskDelete') === 'true';

    deleteForms.forEach(button => {
        button.addEventListener('click', function(event) {
            if (dontAsk) {
                return; // Borrar directamente si ya no quiere preguntar
            }
            event.preventDefault();
            currentForm = button.closest('form');
            deleteModal.show();
        });
    });

    document.getElementById('confirmDeleteBtn').addEventListener('click', () => {
        if (document.getElementById('dontAskAgain').checked) {
            localStorage.setItem('dontAskDelete', 'true');
        }
        if (currentForm) {
            currentForm.submit();
        }
        deleteModal.hide();
    });
});


// Aquí puedes agregar más funcionalidades JS como:
// - Mostrar un toast al marcar completada
// - Animaciones de tarjetas
// - Filtrar tareas por completadas/no completadas
