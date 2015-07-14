class Stack():
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


while True:
    L=int(raw_input())
    if L==0:
        break
    arr=map(int,raw_input().split())
    lane=Stack()
    need=1
    state=True
    for i in range(L):
        while (not lane.isEmpty()) and lane.peek() == need:
            need+=1
            lane.pop()

        if arr[i] == need:
            need+=1
        elif (not lane.isEmpty()) and lane.peek() < arr[i]:
            state=False
            break
        else:
            lane.push(arr[i])

    if state:
        print "yes"
    else:
        print "no"