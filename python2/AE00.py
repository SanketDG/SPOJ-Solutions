n=int(raw_input())
s=0
for i in range(1, int(n**0.5)+1):
    temp=n//i-i+1
    s+=temp
print s