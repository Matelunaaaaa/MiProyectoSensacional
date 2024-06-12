document.addEventListener("DOMContentLoaded", () => {
    const contenido = document.getElementById("contenido");

    // URL de la API
    const url = "https://api.thedogapi.com/v1/breeds";
    const limite = 10; // Número de resultados que queremos mostrar

    // Llamada a la API utilizando fetch
    fetch(url)
        .then(response => response.json())
        .then(data => {
            // Limitar los resultados a los primeros limite elementos
            const limitedData = data.slice(0, limite);

            // Procesar los datos recibidos de la API
            let output = "<ul>";
            limitedData.forEach(breed => {
                output += `<li><strong>Nombre de la Raza:</strong> ${breed.name} <br> <strong>Temperamento:</strong> ${breed.temperament}</li>`;
            });
            output += "</ul>";

            // Mostrar los datos en el HTML
            contenido.innerHTML = output;
        })
        .catch(error => {
            console.error("Error al llamar a la API:", error);
            contenido.innerHTML = "Ocurrió un error al obtener los datos.";
        });
});