for _ in xrange(int(raw_input())):
    x=raw_input()
    n=raw_input()
    a,r=n.split('=')
    a1,a2=str(a).split('+')
    if "machula" in r:
        a1=int(a1)
        a2=int(a2)
        print "%s + %s = %s"%(a1,a2,a1+a2)
    elif "machula" in a1:
        r=int(r)
        a2=int(a2)
        print "%s + %s = %s"%(r-a2,a2,r)
    else:
        a1=int(a1)
        r=int(r)
        print "%s + %s = %s"%(a1,r-a1,r)



