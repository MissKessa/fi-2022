def square():
    n=int(input("length of the square: "))
    for i in range (0,n,1):
        for j in range(0,n,1):
            print("*",end="")
        print()


def square2():
    n=int(input("length of the square: "))
    l=""
    for i in range (0,n,1):
        for j in range(0,n,1):
            l+="*"
        l+="\n"
    print(l)

def rectangle():
    n=int(input("height of the rectangle: "))
    h=int(input("length of the rectangle: "))
    for i in range (0,n,1):
        for j in range(0,h,1):
            print("*",end="")
        print()

def triangle():
    n=int(input("length of the triangle: "))
    for i in range (0,n,1):
        for j in range(0,i+1,1):
            print("*",end="")
        print()

def empty_triangle():
    n=int(input("length of the triangle: "))
    for i in range (0,n,1):
        for j in range(0,i+1,1):
            if j==0 or j==i or i==n-1:
                c="*"
            else:
                c=" "
            print(c,end="")
        print()

def triangle_right():
    n=int(input("length of the triangle: "))
    for i in range (0,n+1,1):
        for j in range(0,n-i,1):
            print(" ",end="")
        for j in range(n-i,n,1):
            print("*",end="")
        print()

def pyramid():
    n=int(input("length of the triangle: "))
    for i in range (0,n,1):
        for j in range(0,n-i-1,1):
            print(" ",end="")
        for j in range(n-i-1,n,1):
            print("*",end="")
        for j in range(0,i,1):
            print("*",end="")
        print()
