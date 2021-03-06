#!/usr/bin/env python

#
# Measurements:
#
# --- t0 ------ t1 ------ t2 ------ t3 ------ t4 ------ t5 ------ t6 ------ t7 -------
a = [ 1817783,  2297702,  2597245,  2769924,  3069245,  3241939,  3541245,  4021134 ]
b = [ 5031146,  5511045,  5811245,  5983939,  6283245,  6455939,  6755245,  7235134 ]
c = [ 8244979,  8724880,  9024245,  9196939,  9496245,  9668939,  9968245,  10448134 ]
d = [ 11457973, 11937865, 12237245, 12409939, 12709245, 12881939, 13181245, 13661134 ]
e = [ 14670991, 15150880, 15450245, 15622924, 15922245, 16094939, 16394245, 16874134 ]
f = [ 17883986, 18363880, 18663245, 18835939, 19135245, 19307939, 19607245, 20087134 ]
g = [ 21096971, 21576865, 21876245, 22048939, 22348245, 22520924, 22820245, 23300134 ]
h = [ 24309990, 24789880, 25089245, 25261924, 25561245, 25733939, 26033245, 26513134 ]
i = [ 27522990, 28002880, 28302245, 28474924, 28774245, 28946939, 29246245, 29726134 ]
j = [ 30736026, 31215909, 31515245, 31687939, 31987245, 32159939, 32459245, 32939134 ]

# t1 = t0 + 300*s + q      t2 = t1 + 300*m
# t3 = t2 + 100*s + q      t4 = t3 + 300*m
# t5 = t4 + 100*s + q      t6 = t5 + 300*m
# t7 = t6 + 300*s + q

# `s' = ticks per send unit
# `m' = ticks per microsecond

s300q = [
    a[1] - a[0], a[7] - a[6],
    b[1] - b[0], b[7] - b[6],
    c[1] - c[0], c[7] - c[6],
    d[1] - d[0], d[7] - d[6],
    e[1] - e[0], e[7] - e[6],
    f[1] - f[0], f[7] - f[6],
    g[1] - g[0], g[7] - g[6],
    h[1] - h[0], h[7] - h[6],
    i[1] - i[0], i[7] - i[6],
    j[1] - j[0], j[7] - j[6],
]
s100q = [
    a[3] - a[2], a[5] - a[4],
    b[3] - b[2], b[5] - b[4],
    c[3] - c[2], c[5] - c[4],
    d[3] - d[2], d[5] - d[4],
    e[3] - e[2], e[5] - e[4],
    f[3] - f[2], f[5] - f[4],
    g[3] - g[2], g[5] - g[4],
    h[3] - h[2], h[5] - h[4],
    i[3] - i[2], i[5] - i[4],
    j[3] - j[2], j[5] - j[4],
]
print "s300q =", s300q
print "s100q =", s100q

s300q = float(sum(s300q)) / len(s300q)
s100q = float(sum(s100q)) / len(s100q)
print "s300q =", s300q
print "s100q =", s100q

s = (s300q - s100q) / 200
q = s300q - 300*s
print "s =", s
print "q =", q

m = [
    (a[2] - a[1]) / 300.0, (a[4] - a[3]) / 300.0, (a[6] - a[5]) / 300.0,
    (b[2] - b[1]) / 300.0, (b[4] - b[3]) / 300.0, (b[6] - b[5]) / 300.0,
    (c[2] - c[1]) / 300.0, (c[4] - c[3]) / 300.0, (c[6] - c[5]) / 300.0,
    (d[2] - d[1]) / 300.0, (d[4] - d[3]) / 300.0, (d[6] - d[5]) / 300.0,
    (e[2] - e[1]) / 300.0, (e[4] - e[3]) / 300.0, (e[6] - e[5]) / 300.0,
    (f[2] - f[1]) / 300.0, (f[4] - f[3]) / 300.0, (f[6] - f[5]) / 300.0,
    (g[2] - g[1]) / 300.0, (g[4] - g[3]) / 300.0, (g[6] - g[5]) / 300.0,
    (h[2] - h[1]) / 300.0, (h[4] - h[3]) / 300.0, (h[6] - h[5]) / 300.0,
    (i[2] - i[1]) / 300.0, (i[4] - i[3]) / 300.0, (i[6] - i[5]) / 300.0,
    (j[2] - j[1]) / 300.0, (j[4] - j[3]) / 300.0, (j[6] - j[5]) / 300.0,
]
print "m =", m

m = float(sum(m)) / len(m)
print "m =", m
