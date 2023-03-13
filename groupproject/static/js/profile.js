VANTA.DOTS({
    el: "#profilebg",
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
tl.fromTo('#notfound', {opacity: 0}, {opacity: 1, duration: 1});
tl.fromTo('#notfound', {y:-20}, {y:0, duration: 1}, '<');