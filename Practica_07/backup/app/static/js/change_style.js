let flag = true;

function new_mode() {
    document.getElementById("navigation").className = "navbar navbar-default";
    document.getElementById("btn1").className = "btn btn-success";
    document.getElementById("btn2").className = "btn btn-info";
    document.getElementById("btn3").className = "btn btn-warning";
}

function classic_mode() {
    document.getElementById("navigation").className = "navbar navbar-inverse";
    document.getElementById("btn1").className = "btn btn-primary";
    document.getElementById("btn2").className = "btn btn-danger";
    document.getElementById("btn3").className = "btn btn-success";
}

function change_event() {
    if (flag) {
        new_mode();
        flag = false;
    } else {
        classic_mode();
        flag = true;
    }
}
