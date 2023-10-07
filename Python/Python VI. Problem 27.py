#Python VI. Problem 27
def read_string(message):
    """Checks if the given alphabet has 26 letters"""
    while True:
        a=input(message).strip()
        all_correct=True
        message=""
        for i in range(0,len(a),1):
            if a[i].strip().isalpha():
                message+=a[i]
                continue
            all_correct=False
            break
        
        if all_correct:
            return message
        print("The sentence must include only alphabetic symbols")



def rot13(message):
    """Uses the Caesar cipher to encrypt a
message. The Caesar cipher works like a substitution cipher but each character is replaced
by the character 13 characters to 'its right' in the alphabet"""
    alphabet="abcdefghijklmnopqrstuvwxyz"
    encript=""
    for i in range(0,len(message),1):
        for j in range(0,len(alphabet),1):
            if message[i]==alphabet[j]:
                if j+13>=len(alphabet):
                    encript+=(alphabet[13-(len(alphabet)-j)])
                    break
                encript+=(alphabet[j+13])
                break
    return encript


a=read_string("Write the message: ")
print(rot13(a))