def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [int(i) for i in input("Enter Elements To Be Sorted:").strip().split()]
bubbleSort(arr)

print("Sorted:")
print(arr)
