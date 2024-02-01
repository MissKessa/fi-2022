def check_vowels(w):
    """Checks if a string has 4 vowels (repeated or not, ignoring the case)
    -w: It's a character sequence
    -Returns True if w has 4 vowels"""
    vowels=0
    w=w.lower()
    for i in range(0,len(w),1):
        if w[i]=="a" or w[i]=="e" or w[i]=="i" or w[i]=="o" or w[i]=="u":
            vowels+=1
        if vowels==4:
            return True
    return False


counter=0
while True:
    word=input("Write a word? ").strip()
    if check_vowels(word):
        counter+=1
    if counter==3:
        break