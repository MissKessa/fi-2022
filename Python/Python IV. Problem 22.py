#Python IV. Problem 22
combination=4
counter=0
while True:
    while True:
        tries=input("Write the number of the combination: ")
        if tries.lstrip("-").isdigit():
            break 
    tries=int(tries)
    if tries==combination:
        print("The safe is open")
        break
    counter+=1
    attempts=3-counter
    print("Incorrect combination. Tries left:", attempts)
    if attempts==0:
        print("No more attempts left")
        break
        
    

    
