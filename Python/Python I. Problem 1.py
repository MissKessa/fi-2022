#Python I Problem 1
#a)
print(max (2**15,3**12, 5**10))
#b)
print(bin(ord ("a")))
print(bin(ord("A")))
#c)
print(chr(81))
#d)
print(bin(23))
#e)
r=45.06
i=2
s1="EO" #Can't be trasnformed to a number because it's not
s2="1"
print(type(r))
print(type(i))
print(type(s2))

print(int(r))
print(int(s2))
print(float(i))
print(float(s2))
print(str(r))
print(str(i))
#f)
print(round(3.4,0))
print(round(3.4,2))
print(round(3.4,5))
#g
print(type("Hello")) #Output:String
print(type(hex(100))) #Output:Integer
#h
print(type(1/2)) #Output:float
print(type(1//2)) #Output:integer