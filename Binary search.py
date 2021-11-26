def binary_search(list, item):
	low = 0
	high = len(list)-1
	while low <= high:
		mid = (high+low)//2
		if int(list[mid]) == item:
			return mid
		elif int(list[mid]) > item:
			high = mid-1
		elif int(list[mid]) < item:
			low = mid+1
	return None

list = input().split()
item = int(input())
print (binary_search(list, item))
