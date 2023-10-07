#Python IV. Problem 10
counter_a=0
while True:
    while True:
        character=input("Write a character: ")
        if len(character)==1:
            break
    if character == "a":
        counter_a+=1
    if character == ".":
        break

print("The number of 'a' is",counter_a)

#for i in range (0,lenght+1,1):
    #if sentence[i:i+1:1] == "a":
        #counter_a+=1
    #if sentence[i:i+1:1] ==".":
        #break
