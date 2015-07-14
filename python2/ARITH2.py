for _ in xrange(int(raw_input())):
    raw_input()
    a=raw_input()
    a=a.replace("=","")
    a=a.split()
    x=[]
    r=0
    for i in range(len(a)):
        if a[i].isdigit():
            a[i]=int(a[i])
    for i in range(len(a)):
        sym=a[i]
        if sym == "+":
            a[i+1]=a[i-1]+a[i+1]
        elif sym== "*":
            a[i+1]=a[i-1]*a[i+1]
        elif sym == "-":
            a[i+1]=a[i-1]-a[i+1]
        elif sym == "/":
            a[i+1]=a[i-1]/a[i+1]
    print a[-1]