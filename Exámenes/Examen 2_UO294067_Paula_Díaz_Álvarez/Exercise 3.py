def clean_list(p):
    """Eliminates in each element all the blank spaces at the beginnig and the end
    -p: It's a given list
    -Returns a list without blank spaces at the beggining and the end"""
    for i in range(0,len(p),1):
        p[i]=p[i].strip()
    return p


name_file=input("Where did you store? (with the extension) ").strip()
teams=[]
try:
    f=open(name_file,"r")
    while True:
        line=f.readline()
        if line=="":
            break
        teams.extend(line.split("-"))
finally:
    f.close()

#cleaning (create function)
# for i in range(0,len(teams),1):
#     teams[i]=teams[i].strip()
clean_list(teams)


#taking the goals
goals=0
for i in range (0,len(teams),1):
    # if teams[i][-1].isdigit():
    #     goals+=int(teams[i][-1])
    for j in range(0,len(teams[i]),1): #in case the goals are not at the end
        if teams[i][j].isdigit(): #if it's a number, I sum it to the total goals
            goals+=int(teams[i][j])

print(f"The total goals are: {goals}")