def c2java(s):
    a=list(s)
    if a[0]=="_" or a[-1]=="_":
        return "Error!"
    for i in a:
        if i.isupper():
            return "Error!"
    else:
        b=""
        i=0
        m=a.count("_")
        for i in range(len(a)-m):
            if a[i]=="_":
                if a[i+1]=="_" or a[i+1].isupper():
                    return "Error!"
                    break
                a.remove(a[i])
                a[i]=a[i].capitalize()
        return "".join(a)

def java2c(x):
    x=list(x)
    c=0
    if x[0].isupper():
        return "Error!"
    else:
        for i in x:
            if i.isupper():
                c+=1
        for i in range(len(x)+c):
            if x[i].isupper():
                x[i]=x[i].lower()
                x.insert(i,"_")
        return "".join(x)

while True:
    try:
        n=raw_input()
        if n.count("_")>=1:
            print c2java(n)
        else:
            print java2c(n)
    except:
        break