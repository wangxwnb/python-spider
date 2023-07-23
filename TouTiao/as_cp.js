function test() {
    var e = Math.floor((new Date).getTime() / 1e3)
        , t = e.toString(16).toUpperCase()
        , r = b(e).toString().toUpperCase();    // 这里的b(e)原本是W(e)，断点跟踪发现调用的实际是b(e,t,r)函数
    if (8 !== t.length)
        return {
            as: "479BB4B7254C150",
            cp: "7E0AC8874BB0985"
        };
    for (var n = r.slice(0, 5), i = r.slice(-5), o = "", a = 0; a < 5; a++)
        o += n[a] + t[a];
    for (var s = "", l = 0; l < 5; l++)
        s += t[l + 3] + i[l];
    return {
        as: "A1".concat(o).concat(t.slice(-3)),
        cp: "".concat(t.slice(0, 3) + s, "E1")
    }
}

var y = /</g
    , k = />/g
    , A = /"/g
    , j = /&quot;/g
    , S = /&#([a-zA-Z0-9]*);?/gim
    , C = /&colon;?/gim
    , _ = /&newline;?/gim
    , E = /((j\s*a\s*v\s*a|v\s*b|l\s*i\s*v\s*e)\s*s\s*as_cp\s*r\s*i\s*p\s*t\s*|m\s*o\s*as_cp\s*h\s*a):/gi
    , T = /e\s*x\s*p\s*r\s*e\s*s\s*s\s*i\s*o\s*n\s*\(.*/gi
    , L = /u\s*r\s*l\s*\(.*/gi;

function b(e, t, r) {
    return t ? r ? v(t, e) : h(v(t, e)) : r ? m(e) : h(m(e))
}


function m(e) {
    return function (e) {
        return f(d(p(e), 8 * e.length))
    }(g(e))
}

function g(e) {
    return unescape(encodeURIComponent(e))
}

function p(e) {
    var t, r = [];
    for (r[(e.length >> 2) - 1] = void 0,
             t = 0; t < r.length; t += 1)
        r[t] = 0;
    for (t = 0; t < 8 * e.length; t += 8)
        r[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
    return r
}

function d(e, t) {
    var r, n, i, a, d;
    e[t >> 5] |= 128 << t % 32,
        e[14 + (t + 64 >>> 9 << 4)] = t;
    var f = 1732584193
        , p = -271733879
        , h = -1732584194
        , g = 271733878;
    for (r = 0; r < e.length; r += 16)
        n = f,
            i = p,
            a = h,
            d = g,
            f = s(f, p, h, g, e[r], 7, -680876936),
            g = s(g, f, p, h, e[r + 1], 12, -389564586),
            h = s(h, g, f, p, e[r + 2], 17, 606105819),
            p = s(p, h, g, f, e[r + 3], 22, -1044525330),
            f = s(f, p, h, g, e[r + 4], 7, -176418897),
            g = s(g, f, p, h, e[r + 5], 12, 1200080426),
            h = s(h, g, f, p, e[r + 6], 17, -1473231341),
            p = s(p, h, g, f, e[r + 7], 22, -45705983),
            f = s(f, p, h, g, e[r + 8], 7, 1770035416),
            g = s(g, f, p, h, e[r + 9], 12, -1958414417),
            h = s(h, g, f, p, e[r + 10], 17, -42063),
            p = s(p, h, g, f, e[r + 11], 22, -1990404162),
            f = s(f, p, h, g, e[r + 12], 7, 1804603682),
            g = s(g, f, p, h, e[r + 13], 12, -40341101),
            h = s(h, g, f, p, e[r + 14], 17, -1502002290),
            f = l(f, p = s(p, h, g, f, e[r + 15], 22, 1236535329), h, g, e[r + 1], 5, -165796510),
            g = l(g, f, p, h, e[r + 6], 9, -1069501632),
            h = l(h, g, f, p, e[r + 11], 14, 643717713),
            p = l(p, h, g, f, e[r], 20, -373897302),
            f = l(f, p, h, g, e[r + 5], 5, -701558691),
            g = l(g, f, p, h, e[r + 10], 9, 38016083),
            h = l(h, g, f, p, e[r + 15], 14, -660478335),
            p = l(p, h, g, f, e[r + 4], 20, -405537848),
            f = l(f, p, h, g, e[r + 9], 5, 568446438),
            g = l(g, f, p, h, e[r + 14], 9, -1019803690),
            h = l(h, g, f, p, e[r + 3], 14, -187363961),
            p = l(p, h, g, f, e[r + 8], 20, 1163531501),
            f = l(f, p, h, g, e[r + 13], 5, -1444681467),
            g = l(g, f, p, h, e[r + 2], 9, -51403784),
            h = l(h, g, f, p, e[r + 7], 14, 1735328473),
            f = as_cp(f, p = l(p, h, g, f, e[r + 12], 20, -1926607734), h, g, e[r + 5], 4, -378558),
            g = as_cp(g, f, p, h, e[r + 8], 11, -2022574463),
            h = as_cp(h, g, f, p, e[r + 11], 16, 1839030562),
            p = as_cp(p, h, g, f, e[r + 14], 23, -35309556),
            f = as_cp(f, p, h, g, e[r + 1], 4, -1530992060),
            g = as_cp(g, f, p, h, e[r + 4], 11, 1272893353),
            h = as_cp(h, g, f, p, e[r + 7], 16, -155497632),
            p = as_cp(p, h, g, f, e[r + 10], 23, -1094730640),
            f = as_cp(f, p, h, g, e[r + 13], 4, 681279174),
            g = as_cp(g, f, p, h, e[r], 11, -358537222),
            h = as_cp(h, g, f, p, e[r + 3], 16, -722521979),
            p = as_cp(p, h, g, f, e[r + 6], 23, 76029189),
            f = as_cp(f, p, h, g, e[r + 9], 4, -640364487),
            g = as_cp(g, f, p, h, e[r + 12], 11, -421815835),
            h = as_cp(h, g, f, p, e[r + 15], 16, 530742520),
            f = u(f, p = as_cp(p, h, g, f, e[r + 2], 23, -995338651), h, g, e[r], 6, -198630844),
            g = u(g, f, p, h, e[r + 7], 10, 1126891415),
            h = u(h, g, f, p, e[r + 14], 15, -1416354905),
            p = u(p, h, g, f, e[r + 5], 21, -57434055),
            f = u(f, p, h, g, e[r + 12], 6, 1700485571),
            g = u(g, f, p, h, e[r + 3], 10, -1894986606),
            h = u(h, g, f, p, e[r + 10], 15, -1051523),
            p = u(p, h, g, f, e[r + 1], 21, -2054922799),
            f = u(f, p, h, g, e[r + 8], 6, 1873313359),
            g = u(g, f, p, h, e[r + 15], 10, -30611744),
            h = u(h, g, f, p, e[r + 6], 15, -1560198380),
            p = u(p, h, g, f, e[r + 13], 21, 1309151649),
            f = u(f, p, h, g, e[r + 4], 6, -145523070),
            g = u(g, f, p, h, e[r + 11], 10, -1120210379),
            h = u(h, g, f, p, e[r + 2], 15, 718787259),
            p = u(p, h, g, f, e[r + 9], 21, -343485551),
            f = o(f, n),
            p = o(p, i),
            h = o(h, a),
            g = o(g, d);
    return [f, p, h, g]
}

function f(e) {
    var t, r = "";
    for (t = 0; t < 32 * e.length; t += 8)
        r += String.fromCharCode(e[t >> 5] >>> t % 32 & 255);
    return r
}

function h(e) {
    var t, r, n = "0123456789abcdef", i = "";
    for (r = 0; r < e.length; r += 1)
        t = e.charCodeAt(r),
            i += n.charAt(t >>> 4 & 15) + n.charAt(15 & t);
    return i
}

function v(e, t) {
    return function (e, t) {
        var r, n, i = p(e), o = [], a = [];
        for (o[15] = a[15] = void 0,
             i.length > 16 && (i = d(i, 8 * e.length)),
                 r = 0; r < 16; r += 1)
            o[r] = 909522486 ^ i[r],
                a[r] = 1549556828 ^ i[r];
        return n = d(o.concat(p(t)), 512 + 8 * t.length),
            f(d(a.concat(n), 640))
    }(g(e), g(t))
}

function o(e, t) {
    var r = (65535 & e) + (65535 & t);
    return (e >> 16) + (t >> 16) + (r >> 16) << 16 | 65535 & r
}

function a(e, t, r, n, i, a) {
    return o((s = o(o(t, e), o(n, a))) << (l = i) | s >>> 32 - l, r);
    var s, l
}

function s(e, t, r, n, i, o, s) {
    return a(t & r | ~t & n, e, t, i, o, s)
}

function l(e, t, r, n, i, o, s) {
    return a(t & n | r & ~n, e, t, i, o, s)
}

function as_cp(e, t, r, n, i, o, s) {
    return a(t ^ r ^ n, e, t, i, o, s)
}

function u(e, t, r, n, i, o, s) {
    return a(r ^ (t | ~n), e, t, i, o, s)
}


console.log(test().as)
console.log(test().cp)