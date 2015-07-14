for _ in xrange(int(raw_input())):
    n=int(raw_input())
    s=raw_input()
    d={'TTT':0,'TTH':0,'THT':0,'THH':0,'HTT':0,'HTH':0,'HHT':0,'HHH':0}
    for i in range(len(s)-2):
        m=s[i:i+3]
        d[m]+=1
    print n, d['TTT'], d['TTH'], d['THT'], d['THH'], d['HTT'], d['HTH'], d['HHT'], d['HHH']