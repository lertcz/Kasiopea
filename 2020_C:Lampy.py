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
    intRow = []
    for j in range(len(numRow)):
        intRow.append(int(numRow[j]))
    intRow.sort()
    log("iR {}".format(intRow))

    #-------------------------------------
    MAX = 0
    temp = []
    for x in range(int(N)-1):
        if((intRow[x+1] - intRow[x]) > MAX):
            MAX = intRow[x+1] - intRow[x]
            temp.append(MAX)
    log("t {}, {}".format(temp, MAX))
    
    answers.append(max(temp)/2)

    #-------------------------------------

for x in range(len(answers)):
    print(answers[x])
