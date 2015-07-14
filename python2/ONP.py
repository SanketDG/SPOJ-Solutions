T=int(raw_input())
for _ in xrange(T):
    str=raw_input()
    prec={"^":4,"*":3,"/":3,"+":2,"-":2,"(":1}
    opstack=[]
    postFixList=[]
    tokenList=list(str)
    for token in tokenList:
        if token in "abcdefghijklmnopqrstuvwxyz123456789":
            postFixList.append(token)
        elif token=="(":
            opstack.append(token)
        elif token==")":
            toptoken=opstack.pop()
            while toptoken!="(":
                postFixList.append(toptoken)
                toptoken=opstack.pop()
        else:
            while (not opstack==[]) and (prec[opstack[-1]]>=prec[token]):
                postFixList.append(opstack.pop())
            opstack.append(token)
    while not opstack==[]:
            postFixList.append(opstack.pop())
    print "".join(postFixList)

