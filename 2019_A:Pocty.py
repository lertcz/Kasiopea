DEBUG = 0

def log(a):
    if(DEBUG):
        print(a)

T = int(input("T: "))
answers = []
for t in range(T):
    N = int(input("N: "))
    print("Include spaces")
    numRow = input("Numbers: ")
    numRow.split()
    arr = []
    correct = True

    for x in range(0, len(numRow), 2):
        arr.append(numRow[x])
    
    if(len(arr) == N):
        for x in range(N):
            if(int(arr[x]) != x + 1 and int(arr[x]) != 0):
                correct = False
            
            log("debug: " + str(x + 1) + " " + arr[x])

        if(correct):
            answers.append("ANO")
        else:
            answers.append("NE")
    else:
        print("\nN dont equal to number count")

for x in range(len(answers)):
    print(answers[x])
