'''

Input : arr[] = {2, 2, 0, 4, 0, 8}
Output : 4 4 8 0 0 0

Input : arr[] = {0, 2, 2, 2, 0, 6, 6, 0, 0, 8}
Output :  4 2 12 8 0 0 0 0 0 0

'''

def easeTheArray(arr):
    
    count = 0 # Initialize zero
    
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            arr[i] *=2
            arr[i+1] = 0
    
    # Checks if the number is a nonzero.  If it is, then assigns arr[count] = arr[j]
    # and increments count.
    # Otherwise if the number is zero, it skips.  
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[count] = arr[j]
            count = count + 1
    
    
    while count < len(arr):
        arr[count] = 0
        count += 1



arr = [2, 2, 0, 4, 0, 8]

easeTheArray(arr)
#[4,0,0,4,0,8]
print(arr)
