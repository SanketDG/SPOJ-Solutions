while 1:
    n=input()
    if n==-1:
        break
    k=float((-3+pow(-3+12*n,1.0/2))/6)
    d=int(k)
    if d-k==0:
        print "Y"
    else:
        print "N"