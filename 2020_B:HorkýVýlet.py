DEBUG = 0

def log(a):
    if(DEBUG):
        print(a)

T = int(input()) #T
answers = []
for t in range(T):
    N = input()
    numRow = input() #days
    numRow = numRow.split()

    #-------------------------------------
    high = []
    for x in range(int(N)-2):
        temp = []
        temp.append(int(numRow[x]))
        temp.append(int(numRow[x+1]))
        temp.append(int(numRow[x+2]))
        temp.sort()
        high.append(temp)
    
    MAX = 50
    for i in high:
        if(max(i) < MAX):
            MAX = max(i)

    answers.append(MAX)
    #-------------------------------------

for x in range(len(answers)):
    print(answers[x])
