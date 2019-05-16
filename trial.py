import pandas

dk = pandas.read_excel("korela.xlsx", header=None)
nov = dk.loc[0:568, 0:190]

nova2 = nov.drop(1, 1)
i = 2
while i < 567:
    i = i+1
    nova2 = nova2.drop(i, 0)
    i = i+1
    nova2 = nova2.drop(i, 0)
    i = i+1

nova = nov.ix[2, 3]
dk1 = nova2.reset_index(drop=True)
print(dk1)
print(dk1.ix[2, 3])
print(dk.shape)
l = []
l1 = [2]
x = 3
n = dk1.ix[3, 19]
f = 2
print(type(n))
t = True

while x < 189:

    a = dk1.ix[f, x]

    if type(a) == str:
        a = a[:-1]
        if a.find("*") > 0:
            a = float(a[:-1])
        else:
            a = float(a)

    if abs(a) < 0.18:
        for num in l1:
            a = dk1.ix[num, x]

            if type(a) == str:
                a = a[:-1]
                if a.find("*") > 0:
                    a = float(a[:-1])
                else:
                    a = float(a)
            d = 0.18 if x < 50 else 0.18
            if abs(a) < d:
                t = True

            else:
                t = False
                break
        if t:
            l.append(nova2.ix[1, x])

            l1.append(x)
    x = x+1
    if x == 189 and f < 100:
        if len(l) > 10:
            print(l)
            print(len(l))
            print(l1)
        x = 2
        f = f+1
        l1.clear()
        l1.append(2)
        l.clear()
print(l)
print(len(l))
