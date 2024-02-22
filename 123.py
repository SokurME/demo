with open('24_6094.txt') as f:
    s = f.readline()
    m = 0
    a = s.split('XYZY')
    for i in a:
        i = 'ZY' + i + 'XY'
        i = i.replace('XY', '*').replace('ZY', '*')
        k = 0
        for j in range(len(i)):
            if i[j] == '*':
                k += 1
                m = max(m, k)
            else:
                k = 0
    print(m)












