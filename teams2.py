file = open("teams.txt", "r")

outfile=""

for i in range(0,6):
    if i==0:
        outfile+="This is a new line\n"
    elif i>0:
        outfile+=file.readline()
file = open("teams.txt", "w")
file.write(outfile)
file = open("teams.txt", "r")
for i in range(0,6):
    print(file.readline())

file.close()