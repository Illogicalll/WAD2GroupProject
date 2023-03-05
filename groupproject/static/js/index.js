const introAnim = gsap.timeline({onComplete: textTop});

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function showButtons() {
    gsap.fromTo('#buttons', {opacity:0},{opacity:1,ease:"slow(0.7, 0.7, false)", duration:2});
}

function textTop() {
    var pos = text.getBoundingClientRect();
    $('#text').appendTo('.navbar');
    var newPos = text.getBoundingClientRect();
    gsap.fromTo('#text', {y:pos.top}, {y:newPos.top+'.navbar'.height/2, ease:"power3.out", duration:2});
    sleep(40);
    showButtons();
}

introAnim.fromTo('#text', {y:-20},{y:0, duration:1})
introAnim.fromTo('#text', {opacity:0},{opacity:1, duration:2},'<')
introAnim.fromTo('#spinner', {opacity:0},{opacity:1,ease:"slow(0.7, 0.7, false)", duration:2}, '<40%')
introAnim.to('#spinner', {opacity:0, duration:2})


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

$("#buying").click(function() {
    window.location.href = "buying.html"
});

$("#selling").click(function() {
    window.location.href = "selling.html"
});