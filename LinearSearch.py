def linear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

lst = [6,1,5,2,4,3]
t = int(input("Enter the element to be found:"))
result = linear(lst, t)
if result != -1:
    print("The  element is found at index :", result)
else:
    print("The element is not in the list.")
