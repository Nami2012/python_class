str = input("Enter the values seperated by space: ")
key = int(input("Enter the key to search: "))

num_str = (str.split(" "))
num_arr = [int(i) for i in num_str]

arr_len = len(num_arr)
first = 0
last = arr_len - 1

while(first<=last):
    mid = (first + last) // 2
    if(num_arr[mid] == key):
        print(key,"found at location",mid)
        quit()
    elif(key < num_arr[mid]):
        last = mid - 1
    else:
        first = mid + 1
print(key,"not found")