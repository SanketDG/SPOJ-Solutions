def add(x,y):
    return x+y

def reverse(num):
    return int(str(num)[::-1])

def main():
    input=raw_input( )
    for i in range(int(input)):
        j=raw_input( )
        num=j.split(' ')
        a=reverse(num[0])
        b=reverse(num[1])
        print reverse(add(a,b))

main()
