t=int(raw_input())
l=1
while l<=t:
        a=map(int,raw_input().split())
        n=map(int,raw_input().split())
        n=sorted(n, reverse=True)
        i=0
        sum=0

        while i<a[1]:
                sum+=n[i]
                i+=1
                if sum>=a[0]:
                        print "Scenario #%d:" %(l)
                        print "%s"%i
                        break
        if sum<a[0]:
                print "Scenario #%d:" %(l)
                print "impossible"
        if not l==t:
                print ""
        l+=1