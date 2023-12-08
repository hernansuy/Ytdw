function descargarVideo() {
    var url = document.getElementById('urlInput').value;

    if (url.trim() === '') {
        mostrarMensaje('Por favor, ingresa una URL válida.');
        return;
    }

    // Lógica de descarga con yt-dlp (similar al código anterior)
    // Asegúrate de manejar la respuesta de la descarga y actualizar el mensaje en consecuencia.

    mostrarMensaje('Descargando video...');
}

function mostrarMensaje(mensaje) {
    document.getElementById('mensaje').innerText = mensaje;
}
