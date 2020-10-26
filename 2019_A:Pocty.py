DEBUG = 0

def log(a):
    if(DEBUG):
        print(a)

T = int(input()) #T
answers = []
for t in range(T):
    N = int(input()) #N
    numRow = input() #numbers
    numRow = numRow.split()
    correct = True
        
    for x in range(N):
        if(int(numRow[x]) != x + 1 and int(numRow[x]) != 0):
            correct = False

    if(correct):
        answers.append("ANO")
    else:
        answers.append("NE")

for x in range(len(answers)):
    print(answers[x])
