VANTA.DOTS({
    el: "#aboutbg",
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

const tl = gsap.timeline();

tl.fromTo('#title', {opacity: 0}, {opacity: 1, duration: 2});
tl.fromTo('#title', {y:-20}, {y:0, duration: 1}, '<');
tl.fromTo('#desc', {opacity: 0}, {opacity: 1, duration: 2}, '<');
tl.fromTo('#desc', {y:20}, {y:0, duration: 1}, '<');
tl.fromTo('.button', {opacity: 0}, {opacity: 1, duration:2}, '<40%');

$("#back").click(function() {
    window.location.href = $("#back").attr("data-url")
});