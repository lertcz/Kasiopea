DEBUG = 0

def log(a):
    if(DEBUG):
        print(a)

T = int(input()) #T
answers = []
highAnswer = 0
for t in range(T):
    N = input()
    numRow = input() #days
    numRow = numRow.split()

    #20 7 13 19 5 | 19
    #18 40 3 | 40
    #10 10 -5 10 -9 11 12 9 9 7 10 | 9 9 7 (9, nejvyssi teplota)
    #
    #1 3 -5 6 10
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
