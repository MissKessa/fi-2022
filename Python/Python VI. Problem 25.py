#Python VI. Problem 25

def read_alphabet(message):
    """Checks if the given alphabet has 26 letters"""
    while True:
        a=input(message).strip()
        if len(a)==26:
            all_correct=True
            alphabet=""
            for i in range(0,26,1):
                if a[i].strip().isalpha():
                    alphabet+=a[i]
                    continue
                all_correct=False
                break
            
            if all_correct:
                return alphabet
            print("The alphabet must include only alphabetic symbols")
        print("The alphabet must have 26 letters")



def substitution(message,alphabet):
    """Your function should take two parameters, the message you want to encrypt, and a
string that represents the mapping of the 26 letters in the alphabet. Your function should
return a string that is the encrypted version of the message"""
    
    good_alphabet="abcdefghijklmnopqrstuvwxyz"
    encript=""

    for i in range (0,len(message),1):
        for j in range(0,len(good_alphabet),1):
            if message[i]==good_alphabet[j]:
                encript+=alphabet[j]
                break
    return encript

a=input("Write your message: ")
b=read_alphabet("Write your alphabet: ")
print(substitution(a,b))