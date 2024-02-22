with open("26_2395.txt") as f:
    s, n = map(int, f.readline().split())
    a = []
    b = []
    for i in f.readlines():
        t = i.split()
        if t[1] == "A":
            a.append(int(t[0]))
        else:
            b.append(int(t[0]))
    a.sort(reverse=True)
    b.sort()
    t = 0
    cou = 0
    while len(a) != 0:
        su = 0
        k = []
        for i in range(len(a)):
            if su + a[i] <= s:
                su += a[i]
                k.append(a[i])
        m = []
        for i in range(len(b)):
            if su + b[i] <= s:
                su += b[i]
                m.append(b[i])
        for i in k:
            a.remove(i)
        cou += len(m)
        for i in m:
            b.remove(i)
        t += 1
    print(t, cou)
