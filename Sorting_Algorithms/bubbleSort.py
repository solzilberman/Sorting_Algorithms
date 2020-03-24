def bubbleSort(arr):
    n = len(arr)
    count = 0
    sw = 0
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
            count+=1     
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                sw +=1
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)

        
    print(sw)         
# Driver code to test above
arr = [5,2,8,9,1,1,0]
 
bubbleSort(arr)
 
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),



