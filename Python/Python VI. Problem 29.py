#Python VI. Problem 29
def string_to_list(sentence):
    letters=[]
    sentence=sentence.strip().lower()
    for i in range (0,len(sentence),1):
        letters.append(sentence[i])
    return letters


def count_letters(sentence):
    letters=string_to_list(sentence)
    counter=[]
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in range(0,len(alphabet),1):
        counter.append(letters.count(alphabet[i]))
    return counter


a=input("Write a sentence: ")
print(string_to_list(a))
print(count_letters(a))