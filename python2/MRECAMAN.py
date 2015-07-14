exists = [0]*5000000
a = [0]*500001
for i in range(1,500001):
  x = a[i-1]-i
  if ((x>0) and (exists[x]==0)):
    a[i] = x
  else:
    a[i] = a[i-1]  + i
  exists[a[i]] = 1

while 1:
  n = int(raw_input())
  if(n==-1): break
  else: print a[n]