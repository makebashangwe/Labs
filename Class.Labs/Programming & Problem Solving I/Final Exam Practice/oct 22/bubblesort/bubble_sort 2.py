def bubble_sort(arr):
    n = len(arr) 
    for i in range(n): # repeat the process n times
        for j in range(0,n-i-1): #ignore the last element 
            if arr[j] > arr[j-1]: #if the element j is greater then the element before it, 
                arr[j], arr[j+1] = arr[j+1], arr[j] #swap their positions in the array
    return arr


