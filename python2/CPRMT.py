while True:
    try:
        s=list(raw_input())
        t=list(raw_input())
        ans=[]
        for i in s:
            if i in t:
                ans.append(i)
                t.remove(i)
        print "".join(sorted(ans))
    except:
        break


