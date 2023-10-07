#Python VI. Problem 22
def lastChars(w1,w2):
    """, receiving two strings and returning a string with the
first symbol of the former and the last one from the latter. If either string is length 0, use
’@’ for its missing char."""
    if len(w1)==0:
        w1="@"
    if len(w2)==0:
        w2="@"
    return w1[0]+w2[-1]


a=input("Write a word: ")
b=input("Write another word: ")
print("The result is:",lastChars(a,b))