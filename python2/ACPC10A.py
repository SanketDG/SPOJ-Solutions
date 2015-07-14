while True:
    T=raw_input()
    if "0 0 0" in T:
        break
    else:
        a=T.split()
        a = map(int, a)
        ap=a[2]-a[1]
        if 2*a[1]==a[0]+a[2]:
            print "AP %s" %(a[2]+ap)
        else:
            gp=int(a[2])/int(a[1])
            print"GP %s" %(a[2]*gp)