
def masala20(n):
    a, c, r = 1, [], []
    while a != n + 1:
        b = int(input(f"{a}-sonni kiriting: "))
        c.append(b)
        a += 1
    for i in range(len(c) - 1):
        if c[i] < c[i+1]:
            r.append(c[i])

    return f"o'ng qo'shnisidan kichkina sonlar: {r}, ularning soni {len(r)} ta"

print(masala20(5))




def masala21(n):
    a, c = 1, []
    while a != n + 1:
        b = int(input(f"{a}-sonni kiriting: "))
        c.append(b)
        a += 1
    if sorted(c) == c:
        return True
    else:
        return False

print(masala21(5))




def masala22(n):
    a, c = 1, []
    while a != n + 1:
        b = int(input(f"{a}-sonni kiriting: "))
        c.append(b)
        a += 1
    if sorted(c)[::-1] == c:
        return 0
    else:
        for i in range(len(c)-1):
            if c[i] <= c[i + 1]:
                return c[i + 1]

print(masala22(5))



def masala23(n):
    a, c = 1, []
    while a != n + 1:
        b = int(input(f"{a}-sonni kiriting: "))
        c.append(b)
        a += 1
    for i in range(len(c)-1):
        s = []
        if not (c[i] < c[i + 1] and c[i + 1] > c[i + 2]):
            return c[i + 2]
    return 0

print(masala23(5))



def masala24(n):
    a, c, r = 1, [], 0
    while a != n + 1:
        b = int(input(f"{a}-sonni kiriting: "))
        c.append(b)
        a += 1
    c.reverse()
    nol1 = c.index(0)
    c1 = c[nol1 + 1:]
    for i in c1:
        if i != 0:
            r += i
        else:
            break
    return r

print(masala24(5))



def masala25(n):
    a, c = 1, []
    while a != n + 1:
        b = int(input(f"{a}-sonni kiriting: "))
        c.append(b)
        a += 1
    nol1 = c.index(0)
    nol2 = c[::-1].index(0)
    r = c[nol1 + 1 : len(c) - 1 - nol2]
    return sum(r)

print(masala25(6))


def masala26(n, k):
    a, c, r = 1, [], []
    while a != n + 1:
        b = int(input(f"{a}-sonni kiriting: "))
        c.append(b)
        a += 1
    for i in c:
        r.append(i ** k)
    return r

print(masala26(5, 2))



def masala27(n):
    a, c = 1, []
    while a != n + 1:
        b = int(input(f"{a}-sonni kiriting: "))
        c.append(b ** a)
        a += 1
    return c

print(masala27(5))



def masala28(n):
    c = []
    while n != 0:
        b = int(input(f"sonni kiriting: "))
        c.append(b ** n)
        n -= 1
    return c

print(masala28(5))



def masala29(n, k):
    r = 0
    while k != 0:
        t = n
        while t != 0:
            a = int(input(f"{k}-to'plamning {n}-elementini kiriting: "))
            r += a
            t -= 1
        k -= 1
    return r


print(masala29(4, 3))
