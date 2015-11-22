##this is a example of how to find squareroots of numbers, if modified correctly
##you may find other valuable numbers lets play
##a/b where n is the root you are looking for and i is the number of iterations
def nmaths(a,b,n,i):

    ###Start values where t is a temperary to swap between and s is a set of values
    t=0
    na=0
    nb=0
    ###define rules here,
    while i >0:
        t=(a+b)
        b=((b+4*a)+b)
        a=t
        i -= 1
        if i == 1:
            na = a
            nb = b

    print(na)
    print(nb)
    #print(bl)
    return na/nb

print(nmaths(1,1,2,30))
