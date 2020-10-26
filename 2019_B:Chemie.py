# F > 1
# R > 0
# 1 + 1 > 0
# 0 + 0 > 0
# 1 + 0 > 1 | 0 + 1 > 1
DEBUG = 0

def debug(a):
    if(DEBUG):
        print(a)


T = int(input()) #T:
answers = []
for t in range(T):
    TEMP = input() #Rows M: Collumns N:
    TEMP = TEMP.split()
    M = int(TEMP[0])
    N = int(TEMP[1])
    
    arr = []
    for x in range(M):
        arr1 = []
        numRow = input() #Molecules:
        numRow = numRow.split()

        arr.append(numRow)
    
    for i in range(M-1):
        arr2 = []
        debug(arr)
        for j in range(N):
#             1st optimalization / expensive way
#             if(arr[i][j] == "1" and arr[i+1][j] == "1"):
#                 arr2 += '0'
#             elif(arr[i][j] == "0" and arr[i+1][j] == "0"):
#                 arr2 += '0'
#             elif((arr[i][j] == "0" and arr[i+1][j] == "1") or (arr[i][j] == "1" and arr[i+1][j] == "0")):
#                 arr2 += '1'

#             2nd optimalization

#             arr2 += str(abs(int(arr[i][j]) - int(arr[i+1][j])))

#           Use of XOR 
            arr2 += str( int(arr[i][j]) ^ int(arr[i+1][j]) )
            
        arr[i+1] = arr2

    for x in arr[-1]:
        print(x, end = ' ')
    print("\n")
