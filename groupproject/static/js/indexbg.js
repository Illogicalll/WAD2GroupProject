// VANTA.JS
! function(t, e) {
    "object" == typeof exports && "object" == typeof module ? module.exports = e() : "function" == typeof define && define.amd ? define([], e) : "object" == typeof exports ? exports._vantaEffect = e() : t._vantaEffect = e()
}("undefined" != typeof self ? self : this, (() => (() => {
    "use strict";
    var t = {
            d: (e, i) => {
                for (var s in i) t.o(i, s) && !t.o(e, s) && Object.defineProperty(e, s, {
                    enumerable: !0,
                    get: i[s]
                })
            },
            o: (t, e) => Object.prototype.hasOwnProperty.call(t, e),
            r: t => {
                "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {
                    value: "Module"
                }), Object.defineProperty(t, "__esModule", {
                    value: !0
                })
            }
        },
        e = {};

    function i(t, e) {
        return null == t && (t = 0), null == e && (e = 1), t + Math.random() * (e - t)
    }
    t.r(e), t.d(e, {
        default: () => d
    }), Number.prototype.clamp = function(t, e) {
        return Math.min(Math.max(this, t), e)
    };

    function s(t) {
        for (; t.children && t.children.length > 0;) s(t.children[0]), t.remove(t.children[0]);
        t.geometry && t.geometry.dispose(), t.material && (Object.keys(t.material).forEach((e => {
            t.material[e] && null !== t.material[e] && "function" == typeof t.material[e].dispose && t.material[e].dispose()
        })), t.material.dispose())
    }
    const o = "object" == typeof window;
    let n = o && window.THREE || {};
    o && !window.VANTA && (window.VANTA = {});
    const r = o && window.VANTA || {};
    r.register = (t, e) => r[t] = t => new e(t), r.version = "0.5.24";
    const h = function() {
        return Array.prototype.unshift.call(arguments, "[VANTA]"), console.error.apply(this, arguments)
    };
    r.VantaBase = class {
        constructor(t = {}) {
            if (!o) return !1;
            r.current = this, this.windowTouchWrapper = this.windowTouchWrapper.bind(this), this.resize = this.resize.bind(this), this.animationLoop = this.animationLoop.bind(this), this.restart = this.restart.bind(this);
            const e = "function" == typeof this.getDefaultOptions ? this.getDefaultOptions() : this.defaultOptions;
            if (this.options = Object.assign({
                    mouseControls: !0,
                    touchControls: !0,
                    gyroControls: !1,
                    minHeight: 200,
                    minWidth: 200,
                    scale: 1,
                    scaleMobile: 1
                }, e), (t instanceof HTMLElement || "string" == typeof t) && (t = {
                    el: t
                }), Object.assign(this.options, t), this.options.THREE && (n = this.options.THREE), this.el = this.options.el, null == this.el) h('Instance needs "el" param!');
            else if (!(this.options.el instanceof HTMLElement)) {
                const t = this.el;
                if (this.el = (i = t, document.querySelector(i)), !this.el) return void h("Cannot find element", t)
            }
            var i, s;
            this.prepareEl(), this.initThree(), this.setSize();
            try {
                this.init()
            } catch (t) {
                return h("Init error", t), this.renderer && this.renderer.domElement && this.el.removeChild(this.renderer.domElement), void(this.options.backgroundColor && (console.log("[VANTA] Falling back to backgroundColor"), this.el.style.background = (s = this.options.backgroundColor, "number" == typeof s ? "#" + ("00000" + s.toString(16)).slice(-6) : s)))
            }
            this.resize(), this.animationLoop();
            const a = window.addEventListener;
            a("resize", this.resize), window.requestAnimationFrame(this.resize), this.options.touchControls && (a("touchstart", this.windowTouchWrapper), a("touchmove", this.windowTouchWrapper)), this.options.gyroControls && a("deviceorientation", this.windowGyroWrapper)
        }
        setOptions(t = {}) {
            Object.assign(this.options, t)
        }
        prepareEl() {
            let t, e;
            if ("undefined" != typeof Node && Node.TEXT_NODE)
                for (t = 0; t < this.el.childNodes.length; t++) {
                    const e = this.el.childNodes[t];
                    if (e.nodeType === Node.TEXT_NODE) {
                        const t = document.createElement("span");
                        t.textContent = e.textContent, e.parentElement.insertBefore(t, e), e.remove()
                    }
                }
            for (t = 0; t < this.el.children.length; t++) e = this.el.children[t], "static" === getComputedStyle(e).position && (e.style.position = "relative"), "auto" === getComputedStyle(e).zIndex && (e.style.zIndex = 1);
            "static" === getComputedStyle(this.el).position && (this.el.style.position = "relative")
        }
        applyCanvasStyles(t, e = {}) {
            Object.assign(t.style, {
                position: "absolute",
                zIndex: 0,
                top: 0,
                left: 0,
                background: ""
            }), Object.assign(t.style, e), t.classList.add("vanta-canvas")
        }
        initThree() {
            n.WebGLRenderer ? (this.renderer = new n.WebGLRenderer({
                alpha: !0,
                antialias: !0
            }), this.el.appendChild(this.renderer.domElement), this.applyCanvasStyles(this.renderer.domElement), isNaN(this.options.backgroundAlpha) && (this.options.backgroundAlpha = 1), this.scene = new n.Scene) : console.warn("[VANTA] No THREE defined on window")
        }
        getCanvasElement() {
            return this.renderer ? this.renderer.domElement : this.p5renderer ? this.p5renderer.canvas : void 0
        }
        getCanvasRect() {
            const t = this.getCanvasElement();
            return !!t && t.getBoundingClientRect()
        }
        windowTouchWrapper(t) {
            const e = this.getCanvasRect();
            if (!e) return !1;
            if (1 === t.touches.length) {
                const i = t.touches[0].clientX - e.left,
                    s = t.touches[0].clientY - e.top;
                i >= 0 && s >= 0 && i <= e.width && s <= e.height && (this.mouseX = i, this.mouseY = s, this.options.mouseEase || this.triggerMouseMove(i, s))
            }
        }
        setSize() {
            this.scale || (this.scale = 1), "undefined" != typeof navigator && (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) || window.innerWidth < 600) && this.options.scaleMobile ? this.scale = this.options.scaleMobile : this.options.scale && (this.scale = this.options.scale), this.width = Math.max(this.el.offsetWidth, this.options.minWidth), this.height = Math.max(this.el.offsetHeight, this.options.minHeight)
        }
        resize() {
            this.setSize(), this.camera && (this.camera.aspect = this.width / this.height, "function" == typeof this.camera.updateProjectionMatrix && this.camera.updateProjectionMatrix()), this.renderer && (this.renderer.setSize(this.width, this.height), this.renderer.setPixelRatio(window.devicePixelRatio / this.scale)), "function" == typeof this.onResize && this.onResize()
        }
        isOnScreen() {
            const t = this.el.offsetHeight,
                e = this.el.getBoundingClientRect(),
                i = window.pageYOffset || (document.documentElement || document.body.parentNode || document.body).scrollTop,
                s = e.top + i;
            return s - window.innerHeight <= i && i <= s + t
        }
        animationLoop() {
            this.t || (this.t = 0), this.t2 || (this.t2 = 0);
            const t = performance.now();
            if (this.prevNow) {
                let e = (t - this.prevNow) / (1e3 / 60);
                e = Math.max(.2, Math.min(e, 5)), this.t += e, this.t2 += (this.options.speed || 1) * e, this.uniforms && (this.uniforms.iTime.value = .016667 * this.t2)
            }
            return this.prevNow = t, (this.isOnScreen() || this.options.forceAnimate) && ("function" == typeof this.onUpdate && this.onUpdate(), this.scene && this.camera && (this.renderer.render(this.scene, this.camera), this.renderer.setClearColor(this.options.backgroundColor, this.options.backgroundAlpha)), this.fps && this.fps.update && this.fps.update(), "function" == typeof this.afterRender && this.afterRender()), this.req = window.requestAnimationFrame(this.animationLoop)
        }
        restart() {
            if (this.scene)
                for (; this.scene.children.length;) this.scene.remove(this.scene.children[0]);
            "function" == typeof this.onRestart && this.onRestart(), this.init()
        }
        init() {
            "function" == typeof this.onInit && this.onInit()
        }
        destroy() {
            "function" == typeof this.onDestroy && this.onDestroy();
            const t = window.removeEventListener;
            t("touchstart", this.windowTouchWrapper), t("touchmove", this.windowTouchWrapper), t("deviceorientation", this.windowGyroWrapper), t("resize", this.resize), window.cancelAnimationFrame(this.req);
            const e = this.scene;
            e && e.children && s(e), this.renderer && (this.renderer.domElement && this.el.removeChild(this.renderer.domElement), this.renderer = null, this.scene = null), r.current === this && (r.current = null)
        }
    };
    const a = r.VantaBase;
    let l = "object" == typeof window && window.THREE;
    class c extends a {
        static initClass() {
            this.prototype.defaultOptions = {
                color: 16746528,
                color2: 16746528,
                backgroundColor: 2236962,
                size: 3,
                spacing: 35,
                showLines: !0
            }
        }
        onInit() {
            var t = this.camera = new l.PerspectiveCamera(10, this.width / this.height, .1, 5e3);
            t.position.x = 0, t.position.y = 250, t.position.z = 500, t.tx = 0, t.ty = 50, t.tz = 150, t.lookAt(0, 0, 0), this.scene.add(t);
            var e, s, o, n, r, h, a, c = this.starsGeometry = new l.BufferGeometry,
                d = this.options.spacing;
            const p = [];
            for (e = o = -30; o <= 30; e = ++o)
                for (s = n = -30; n <= 30; s = ++n)(r = new l.Vector3).x = e * d + d / 2, r.y = i(0, 5) - 150, r.z = s * d + d / 2, p.push(r);
            if (c.setFromPoints(p), h = new l.PointsMaterial({
                    color: this.options.color,
                    size: this.options.size
                }), a = this.starField = new l.Points(c, h), this.scene.add(a), this.options.showLines) {
                var u = new l.LineBasicMaterial({
                        color: this.options.color2
                    }),
                    m = new l.BufferGeometry;
                const t = [];
                for (e = 0; e < 200; e++) {
                    var f = i(40, 60),
                        w = f + i(12, 20),
                        g = i(-1, 1),
                        y = Math.sqrt(1 - g * g),
                        v = i(0, 2 * Math.PI),
                        M = Math.sin(v) * y,
                        b = Math.cos(v) * y;
                    t.push(new l.Vector3(b * f, M * f, g * f)), t.push(new l.Vector3(b * w, M * w, g * w))
                }
                m.setFromPoints(t), this.linesMesh = new l.LineSegments(m, u), this.scene.add(this.linesMesh)
            }
        }
        onUpdate() {
            const t = this.starsGeometry;
            this.starField;
            for (var e = 0; e < t.attributes.position.array.length; e += 3) {
                const i = t.attributes.position.array[e],
                    s = t.attributes.position.array[e + 1],
                    o = t.attributes.position.array[e + 2],
                    n = s + .1 * Math.sin(.02 * o + .015 * i + .02 * this.t);
                t.attributes.position.array[e + 1] = n
            }
            t.attributes.position.setUsage(l.DynamicDrawUsage), t.computeVertexNormals(), t.attributes.position.needsUpdate = !0;
            const i = this.camera,
                s = .003;
            i.position.x += (i.tx - i.position.x) * s, i.position.y += (i.ty - i.position.y) * s, i.position.z += (i.tz - i.position.z) * s, i.lookAt(0, 0, 0), this.linesMesh && (this.linesMesh.rotation.z += .002, this.linesMesh.rotation.x += 8e-4, this.linesMesh.rotation.y += 5e-4)
        }
        onRestart() {
            this.scene.remove(this.starField)
        }
    }
    c.initClass();
    const d = r.register("DOTS", c);
    return e
})()));