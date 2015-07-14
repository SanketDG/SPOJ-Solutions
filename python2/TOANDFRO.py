while True:
    n=int(raw_input())
    if n==0:
        break
    else:
        s=raw_input()
        b=[]
        i=0
        j=n
        while i<len(s):
            b.append(s[i:j])
            i=j
            j+=n
        for x in range(1,len(b),2):
            b[x]=b[x][::-1]
        k=0
        m=""
        j=0
        while j<n:
            i=0
            while i<len(b):
                m+=b[i][j]
                i+=1
            j+=1
        print m
