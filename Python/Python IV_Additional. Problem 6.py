#Python IV_Additional. Problem 6
A=25000000
B=19900000
years_until=0

while B<A: #years that pass
    A*=1+0.02
    B*=1+0.03
    years_until+=1
print("The population of B will be greater than A's in",years_until,"years")