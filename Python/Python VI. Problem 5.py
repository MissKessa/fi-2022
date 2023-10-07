#Python VI. Problem 5
def sum_elements (list1):
    """Returns the sum of all the elements of a list"""
    result=0
    for i in list1:
       result+=i
    return result

def read_list_integers(message,separator):
    """Reads a list split by the separator and checks if all the elements are integers.
    If it's not a numeric list, it asks again for the list"""
    while True:
        list1=input(message)
        list1=list1.split(separator)
        has_letters=False

        for i in range(0, len(list1),1):
            if list1[i].strip().lstrip("-").isdigit():
                list1[i] = int(list1[i])
            else:
                has_letters=True
                break
        
        if not has_letters:
            return list1
        print("It's not a list of integers")

character=input("what separator are you going to use? ")
list2=read_list_integers("Write a list: ",character)

print("The sum of the element is",sum_elements(list2))
print("The sum of the element is",sum(list2))
