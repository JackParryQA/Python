file = open("teams.txt","r")

for line in range(1,6):
    if line==1 or line==4:
        print(file.readline())
    else:
        file.readline()

file.close()