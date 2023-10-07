#Python 3. Problem 10
mark=float(input("Write your mark:"))
if mark<5:
    print("fail(E)")
elif mark<7:
    print("pass(D)")
elif mark<9:
    print("pass(C)")
elif mark<10:
    print("pass(B)")
else:
    print("pass(A)")