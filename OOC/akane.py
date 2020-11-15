def table(headers,data,width=10):
    y = ''
    space = ' ' * width 
    for i in headers:
        y += i + space
    z = ''
    count = 0
    fam = len(headers)
    for i in data:
        
        if count < fam:
            z += i + space 
            count += 1

        else:
            z += '\n' + i  + space
            count = 1
    
    return (y + '\n' + z)


# x = ['YEAR','STATE','VOTES']
# b = ['1997','alabama','90','1997','california','70','1998','indiana','100']
# print(table(x,b))
def a(n):
    """
    Function must be recursive
    """
    if n == 0:
        return 1
    else:
        return n*((-1)**n) +a(n-1)



def h():
    """
    Must be written as a generator
    """
    x,y = 1,0
    while True:
        yield x
        x,y = y, (x+1)*((-1)**(x+1))

#function ag uses the generator h()
def ag(n):
    """
    Function must utilize the generator
    """
    if n == 0:
        return 0
    else:
        for i in h():
            if i == 0:
                return i
            else:
                yield i
# for i in ag(5):
#     print(i)
# b = h()
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))


def h():
    x = 0
    while True:
        yield x
        x = x+2

def g(xstop):
    for i in h():
        if i > xstop:
            return i
        else:
            yield i
# for i in g(10):
#     print(i)

def cr(n,m):
    """
    Must be recursive
    """
    if m == 0 or n == m:
        return 1
    else:
        return cr(n-1,m) + cr(n-1,m-1)

#recursive
def B(n):
    """
    Must be recursive
    """
    def calc(n):
        if n == 0:
            return 1
        else:
            return -(1/(1+n)) * (cr(n,n)*B(-1))
    if n == 0:
        return 1
    else:
        z = [i for i in range(n+1)]
        x = -(1/(1+n))
        y = [cr(n+1,i) for i in range(n+1)]
        g = []
        for i in y:
            g.append(i*calc(n))
        return sum(g) * x
    print(g)
    # if n == 0:
    #     return 1
    # else:
    #     return  
print(B(3))
