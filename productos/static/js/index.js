
const nombre = document.getElementById("name")
const email = document.getElementById("email")
const rut = document.getElementById("rut")
const problema = document.getElementById("problema")
const form = document.getElementById("form")
const parrafo = document.getElementById("warnings")


// Función para validar un correo electrónico
function validarEmail(email) {
  var emailRegex = /^[\w-.]+@([\w-]+.)+[\w-]{2,4}$/;
  return emailRegex.test(email);
}

// Función para validar rut
function validarRut(rut) {
  var rutRegex = /^(\d{1,2}.)?\d{3}.\d{3}-[\dkK]$/;
  return rutRegex.test(rut);
}

form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    let entrar = false

    if((validarEmail(email.value))==false && entrar == false){
        warnings += `El email no es valido` 
        entrar = true
    }

    if((validarRut(rut.value)) == false && entrar == false){
        warnings += `Rut no valido` 
        entrar = true
    }

    if(nombre.value.length<6 && entrar == false){
      warnings += `El nombre no es valido` 
      entrar = true
    }

    if(problema.value.length<1 && entrar == false){
      warnings += `El parrafo esta vacio` 
      entrar = true
    }

    if(entrar){
      alert(warnings) 
    }else{
        parrafo.innerHTML = "Enviado"
        nombre.value = ""
        rut.value = ""
        email.value = ""
        problema.value = ""
    }
})

