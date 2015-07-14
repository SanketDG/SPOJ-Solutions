while True:
    try:
        n=raw_input()
        if n=="0 0":
            break
        a=map(int,raw_input().split())
        d=map(int,raw_input().split())
        a.sort()
        d.sort()
        if a[0]<d[1]:
            print "Y"
        elif a[0]==d[0]:
            if d.count(d[0])>=2:
                print "N"
            else:
                print "Y"
        elif a[0]<=d[0]:
            print "Y"
        else:
            print "N"
    except:
        break