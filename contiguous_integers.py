# Byron Luo


#Check if array contains contiguous integers with duplicates allowed

#Given an array of n integers(duplicates allowed). 
# Print "Yes" if it is a set of contiguous integers else print "No".

def checkContiguous(listNumber, num):
    for i in range(1, num):    
        if (listNumber[i] - listNumber[i-1]) > 1 :
            return False
    return True

## Main Code

testCase = input()

for t in range(int(testCase)):
    num = int(input())
    arr = [int(x) for x in input().split()]
    sortTest = sorted(arr)

    if checkContiguous(sortTest,num):
        print('Yes')
    else:
        print('No')



