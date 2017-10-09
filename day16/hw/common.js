function login() {
    document.getElementById("i1").classList.remove('hide');
    document.getElementById("i2").classList.remove('hide');
}

function register() {
    document.getElementById("i1").classList.remove('hide');
    document.getElementById("i3").classList.remove('hide');
}

function rm_login() {
    document.getElementById("i2").classList.add('hide');
    document.getElementById("i1").classList.add('hide');
}

function rm_regiter() {
    document.getElementById("i3").classList.add('hide');
    document.getElementById("i1").classList.add('hide');
}

function checkedall() {
    var tbody=document.getElementById('car');
    var tr_list=tbody.children;
    for (var i=0;i<tr_list.length;i++) {
        var current_tr=tr_list[i];
        var checkbox=current_tr.children[0];
        checkbox.checked=true;
    }
}

function cancelall() {
    var tbody=document.getElementById('car');
    var tr_list=tbody.children;
    for (var i=0;i<tr_list.length;i++) {
        var current_tr=tr_list[i];
        var checkbox=current_tr.children[0];
        checkbox.checked=false;
    }
}

function reverseall() {
    var tbody=document.getElementById('car');
    var tr_list=tbody.children;
    for (var i=0;i<tr_list.length;i++) {
        var current_tr=tr_list[i];
        var checkbox=current_tr.children[0];
        if(checkbox.checked==true) {
            checkbox.checked = false;
        }
        else
            checkbox.checked=true;
    }
}