#Python V. Problem 21
def shut_down (s):
    if s=="yes":
        print("Shutting down")
    elif s=="no":
        print("Shutting aborted")
    else:
        print("Sorry")

answer=input("Do you want to shut down the machine? ")
machine=True
shut_down(answer)
if answer=="yes":
    machine=False