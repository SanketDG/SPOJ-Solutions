while True:
    n=int(raw_input())
    if n==0:
        break
    c=0
    while n>=2:
        n/=2
        c+=1
    print c