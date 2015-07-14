from math import log,floor
while True:
        x=raw_input()
        if x=="00e0":
            break
        f,l,_,z=x[0],x[1],x[2],x[3:]
        n=int(f+l+("0"*int(z)))
        lp=2**(floor(log(n,2)))
        print int(1+(n-lp)*2)