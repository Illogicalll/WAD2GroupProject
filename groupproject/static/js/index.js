const introAnim = gsap.timeline({onComplete: textTop});

function textTop() {
    var pos = text.getBoundingClientRect();
    $('#text').appendTo('.navbar');
    var newPos = text.getBoundingClientRect();
    gsap.fromTo('#text', {y:pos.top}, {y:newPos.top+'.navbar'.height/2, ease:"power3.out", duration:2});
}

introAnim.fromTo('#text', {y:-20},{y:0, duration:1})
introAnim.fromTo('#text', {opacity:0},{opacity:1, duration:3.5},'<')
introAnim.fromTo('#spinner', {opacity:0},{opacity:1,ease:"slow(0.7, 0.7, false)", duration:2}, '<40%')
introAnim.to('#spinner', {opacity:0, duration:2})
