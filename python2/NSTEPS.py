T=int(raw_input())
for _ in xrange(T):
    str=raw_input()
    list=str.split()
    x=int(list[0])
    y=int(list[1])
    if x!=y and x-y!=2:
        print "No Number"
    elif x%2==0 and y%2==0 and x>=y:
        print x+y
    else:
        print (x+y)-1