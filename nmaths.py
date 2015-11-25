##this is a example of how to find squareroots of numbers, if modified correctly
##you may find other valuable numbers lets play
##a/b where n is the root you are looking for and i is the number of iterations
def nmaths(a,b,n,i):
    ###Start values where t is a temperary to swap between and s is a set of values
    t=0
    #define rules here,
    while i >1:
        a, b = a+n*b, a+b
        i -= 1
    print(n**(1/2))
    print(a)
    print(b)
    return a/b

print(nmaths(84,84,169,300))
