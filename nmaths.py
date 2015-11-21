##this is a example of how to find squareroots of numbers, if modified correctly
##you may find other valuable numbers lets play
##a/b where n is the root you are looking for and i is the number of iterations
def nmaths(a,b,n,i):

    ###Start values where t is a temperary to swap between and s is a set of values
    t=0
    al=[]
    bl=[]
    ###define rules here,
    while i >0:
        t=(a+n*b)
        b=2*(a+b)
        a=t
        al.append(a)
        bl.append(b)
        i -= 1
    print(al[-1])
    print(bl[-1])
    #print(bl)
    return al[-1]/bl[-1]

print(nmaths(1,1,2,30))
