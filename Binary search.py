def binary_search(arr, item):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (high+low)//2
        if int(arr[mid]) == item:
 	    return mid
        elif int(arr[mid]) > item:
	    high = mid-1
        elif int(arr[mid]) < item:
	    low = mid+1
    return None

arr = []
for i in range(1, 101):
    arr.append(i)
print(arr)

item = int(input())
print (binary_search(arr, item))
