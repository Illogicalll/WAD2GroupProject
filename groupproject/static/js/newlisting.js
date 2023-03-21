VANTA.DOTS({
    el: "#newlistingbg",
    mouseControls: false,
    touchControls: false,
    gyroControls: false,
    minHeight: 50.00,
    minWidth: 50.00,
    scale: 0.50,
    scaleMobile: 1.00,
    color: 0x61ff20,
    color2: 0x0,
    backgroundColor: 0x0,
    size: 4.30,
    spacing: 33.00,
    showLines: false
    });

$('#submit').click(function() {document.forms[0].submit()});
$("#back").click(function() {window.location.href = $("#back").attr("data-url")});
const errorDiv = document.querySelector("#error")
if (document.referrer == "http://127.0.0.1:8000/newlisting/") {
    addErrorMessage();
}

function addErrorMessage() {
    const msg = document.createElement("p");
    msg.innerHTML = "Please Fill Out All Fields";
    $("#error").css("margin-top", "-130px");
    errorDiv.appendChild(msg);
}