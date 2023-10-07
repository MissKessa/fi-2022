#Python VI. Problem 23
def makeTags (tag,word):
    """Function makeTags the web is built with HTML strings like "<i>Yay</i>"
which draws "Yay" as italic text"""
    return "<"+tag+">"+word+"</"+tag+">"

a=input("Write the tag: ")
b=input("Write a word: ")
print(makeTags(a,b))
