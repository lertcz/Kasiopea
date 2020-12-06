DEBUG = 0

def log(a):
    if(DEBUG):
        print(a)

def init_arr(N):
    global N_arr, Visited_arr, Ruler_arr, Assigned_arr
    N_arr = []
    Visited_arr = []
    Ruler_arr = []

    for i in range(N):
        temp_arr = []
        for x in range(N):
            temp_arr.append(0)
        N_arr.append(temp_arr)
    
    for i in range(N):
        Visited_arr.append(0)
        Ruler_arr.append(0)

def search_row(id, Ruler):
    log("search row called id: {} Ruler: {}".format(id,Ruler))
    if(Visited_arr[id] == 0): #int visited
        Visited_arr[id] = 1 # the x changed from id
        Ruler_arr[id] = Ruler
        for x in range(N):
            if(N_arr[id][x] == 1 and Visited_arr[x] == 0): # second x

                #if(Assigned_arr[id] == 0):
                if(Ruler):
                    Ruler = False
                    log("Added ruler")
                else:
                    Ruler = True
                    log("passed")
                
                search_row(x, Ruler)

T = int(input()) #T
answers = []
for t in range(T):
    Ruler = True
    NM = input()
    NM = NM.split() 
    N = int(NM[0]) #pocet lidi
    M = int(NM[1]) #pocet kamaradstvi
    init_arr(N)

    #-------------------------------------
    if(M >= N-1 and M <= N*N):
        for x in range(M):
            Input = input()
            Input = Input.split()
            Num_one = int(Input[0])
            Num_two = int(Input[1])
            N_arr[Num_one - 1][Num_two - 1] = 1
            N_arr[Num_two - 1][Num_one - 1] = 1
        """for i in N_arr:
            print(i)"""

        Min = len(N_arr) + 1
        for x in range(len(N_arr)):
            friends = 0
            for i in range(len(N_arr[x])):
                if(N_arr[x][i] == 1):
                    friends += 1
            if(friends < Min):
                Min = friends
                index = x
        
        log("I/M: " + str(index) + str(Min))

        search_row(index, Ruler)

        log("Rullers: " + str(Ruler_arr))
        log("Visited: " + str(Visited_arr))

        Ruler_count = 0
        Ruler_people_count = []

        for x in range(len(Ruler_arr)):
            if(Ruler_arr[x] == True):
                Ruler_count += 1
                Ruler_people_count.append(x+1)
        
        print("ANO\n" + str(Ruler_count))

        for x in range(len(Ruler_people_count)):
            print(Ruler_people_count[x])


    else:
        for x in range(M):
            pass
        answers.append("NE")
    #-------------------------------------
    
for x in range(len(answers)):
    print(answers[x])