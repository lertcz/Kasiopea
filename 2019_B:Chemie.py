# F > 1
# R > 0
# 1 + 1 > 0
# 0 + 0 > 0
# 1 + 0 > 1 | 0 + 1 > 1
DEBUG = 1 

def debug(a):
    if(DEBUG):
        print(a)


T = int(input("T: "))

for t in range(T):
    M = int(input("\nRows M: "))
    N = int(input("Collumns N: "))
    
    arr = []
    for x in range(M):
        arr1 = []
        numRow = input("Molecules: ")
        numRow.split()
        if(((len(numRow) + 1) >> 1) == N):
            for x in range(0, N+2, 2):
                arr1 += numRow[x]
            
            arr.append(arr1)
        else:
            print("wrong molecule quantity (N)")
            quit()
    
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
    print(arr[-1])
