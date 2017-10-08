function login() {
    document.getElementById("i1").classList.remove('hide')
    document.getElementById("i2").classList.remove('hide')
}

function register() {
    document.getElementById("i1").classList.remove('hide')
    document.getElementById("i3").classList.remove('hide')
}

function rm_login() {
    document.getElementById("i2").classList.add('hide')
    document.getElementById("i1").classList.add('hide')
}

function rm_regiter() {
    document.getElementById("i3").classList.add('hide')
    document.getElementById("i1").classList.add('hide')
}