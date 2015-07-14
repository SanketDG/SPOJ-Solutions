for _ in xrange(int(raw_input())):
    r,c=map(int,raw_input().split())
    if r<=c:
        if r&1==0:
            print "L"
        else:
            print "R"
    else:
        if c&1==0:
            print "U"
        else:
            print "D"