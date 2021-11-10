console.log("ACTIVO");

const botonGuardarMatriz = document.getElementById("boton_guardar_matriz");
botonGuardarMatriz.addEventListener("click", () => {
    const botonAgregarMatriz = document.getElementById("boton_agregar_matriz");
    botonAgregarMatriz.click();
});