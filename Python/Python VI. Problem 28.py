#Python VI. Problem 28
def string_to_list(sentence):
    letters=[]
    sentence=sentence.strip().lower()
    for i in range (0,len(sentence),1):
        letters.append(sentence[i])
    return letters


def count_vocals(sentence):
    letters=string_to_list(sentence)
    counter=[]
    counter.append(letters.count("a"))
    counter.append(letters.count("e"))
    counter.append(letters.count("i"))
    counter.append(letters.count("o"))
    counter.append(letters.count("u"))
    return counter


a=input("Write a sentence: ")
print(string_to_list(a))
print(count_vocals(a))