VANTA.DOTS({
el: "#bg",
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
})

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function showButtons(fast = true) {
    var dur = 5;
    if (fast) {
        dur = 1;
    }
    gsap.fromTo('#buttons', {opacity:0},{opacity:1,ease:"slow(0.7, 0.7, false)", duration:2},'<');
    gsap.fromTo('.button', {opacity:0},{opacity:1,ease:"slow(0.7, 0.7, false)", duration:2});
    gsap.fromTo('#bg', {opacity:0}, {opacity:1,duration:dur})
    $("#buying").css("pointer-events","auto");
    $("#buying").click(function() {
        window.location.href = $("#buying").attr("data-url")
    });
    $("#selling").css("pointer-events","auto");
    $("#selling").click(function() {
        window.location.href = $("#selling").attr("data-url")
    });
    $("#about").css("pointer-events","auto");
    $("#about").click(function() {
        window.location.href = $("#about").attr("data-url")
    });
    $("#login").css("pointer-events","auto");
    $("#login").click(function() {
        window.location.href = $("#login").attr("data-url")
    });
    $("#myprofile").css("pointer-events","auto");
    $("#myprofile").click(function() {
        window.location.href = $("#myprofile").attr("data-url")
    });
    $("#signout").css("pointer-events","auto");
    $("#signout").click(function() { 
        window.location.href = $("#signout").attr("data-url")
    });
    $("#wishlist").css("pointer-events","auto");
    $("#wishlist").click(function() { 
        window.location.href = $("#wishlist").attr("data-url")
    });
}

function textTop() {
    var pos = text.getBoundingClientRect();
    $('#text').appendTo('.navbar');
    var newPos = text.getBoundingClientRect();
    gsap.fromTo('#text', {y:pos.top}, {y:newPos.top+'.navbar'.height/2, ease:"power3.out", duration:2});
    sleep(40);
    showButtons(false);
}

function returning() {
    var pos = text.getBoundingClientRect();
    $('#text').appendTo('.navbar');
    var newPos = text.getBoundingClientRect();
    const returningtl = gsap.timeline({onComplete: showButtons});
    returningtl.fromTo('#text', {opacity:0}, {opacity:1, duration:1});
    returningtl.fromTo('#text', {y:pos.top}, {y:newPos.top+'.navbar'.height/2, ease:"power3.out", duration:1});
}

if (document.referrer == ""){
    const introAnim = gsap.timeline({onComplete: textTop});
    introAnim.fromTo('#text', {y:-20},{y:0, duration:1})
    introAnim.fromTo('#text', {opacity:0},{opacity:1, duration:2},'<')
    introAnim.fromTo('#spinner', {opacity:0},{opacity:1,ease:"slow(0.7, 0.7, false)", duration:2}, '<40%')
    introAnim.to('#spinner', {opacity:0, duration:2})
}
else {
    returning();
}

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