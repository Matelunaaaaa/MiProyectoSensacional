$(document).ready(function() {
  const usuarioid = document.getElementById('id_usuario');
  console.log ('id_usuario ', usuarioid.value)
  if ( usuarioid.value  == '0'){
    $('#headerContent').html('<nav class="navbar navbar-expand-lg navbar-light bg-light"><div class="container"><a class="navbar-brand" href="#">Mundo Animals</a><button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarSupportedContent"><ul class="navbar-nav ml-auto"><li class="nav-item active"><a class="nav-link" href="http://127.0.0.1:8000/productos/Principal/'+ usuarioid.value +'/">Inicio</a></li><li class="nav-item"><a class="nav-link" href="http://127.0.0.1:8000/productos/catalogo/'+ usuarioid.value +'/">Catalogo</a></li><li class="nav-item"><a class="nav-link" href="http://127.0.0.1:8000/productos/registrarse/'+ usuarioid.value +'/">Registrarse</a></li><li class="nav-item"><a class="nav-link" href="http://127.0.0.1:8000/productos/InicioSesion/'+ usuarioid.value +'/">Inicio de sesion</a></li><li class="nav-item"><a class="nav-link" href="http://127.0.0.1:8000/productos/ayuda/'+ usuarioid.value +'/">Ayuda</a></li><li class="nav-item"><a class="nav-link" href="http://127.0.0.1:8000/productos/razas/'+ usuarioid.value +'/">Razas</a></li></ul></div></div></nav>'); // Cargar el contenido del header
    }
  else{
    $('#headerContent').html('<nav class="navbar navbar-expand-lg navbar-light bg-light"><div class="container"><a class="navbar-brand" href="#">Mundo Animals</a><button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarSupportedContent"><ul class="navbar-nav ml-auto"><li class="nav-item active"><a class="nav-link" href="http://127.0.0.1:8000/productos/Principal/'+ usuarioid.value +'/">Inicio</a></li><li class="nav-item"><a class="nav-link" href="http://127.0.0.1:8000/productos/catalogo/'+ usuarioid.value +'/">Catalogo</a></li><li class="nav-item"><a class="nav-link" href="http://127.0.0.1:8000/productos/ayuda/'+ usuarioid.value +'/">Ayuda</a></li><li class="nav-item"><a class="nav-link" href="http://127.0.0.1:8000/productos/razas/'+ usuarioid.value +'/">Razas</a></li></ul></div></div></nav>'); // Cargar el contenido del header
  }
});

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
