VANTA.DOTS({
    el: "#signupbg",
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

const handleMouseMove = e => {
    const {currentTarget:target} = e;
    const rect = target.getBoundingClientRect(),
    x = e.clientX - rect.left,
    y = e.clientY - rect.top;
    target.style.setProperty("--mouse-x", `${x}px`);
    target.style.setProperty("--mouse-y", `${y}px`);
}

for(const button of document.querySelectorAll(".button")) {
    button.onmousemove = e => handleMouseMove(e);
}