DEBUG = 0

def log(a):
    if(DEBUG):
        print(a)

T = int(input()) #T
answers = []
for t in range(T):
    numRow = input() #price   50 30 10 | s reklamou, bez reklamy, cena reklamy
    numRow = numRow.split()
    if((int(numRow[0]) - (int(numRow[1]) + int(numRow[2]))) > 0):
        answers.append("REKLAMU")
    else:
        answers.append("NE REKLAMU")

for x in range(len(answers)):
    print(answers[x])
