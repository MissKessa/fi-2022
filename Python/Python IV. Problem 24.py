#Python IV. Problem 24
while True:
    while True:
        height=input("Write the height: ")
        if height.lstrip("-").isdigit():
            break 
    height=int(height)
    if height>0:
        break
while True:
    while True:
        base=input("Write the base: ")
        if base.lstrip("-").isdigit():
            break 
    base=int(base)
    if base>0:
        break

for i in range (0,height,1):
    for j in range (0,base,1):
        print("*",end="")
    print()