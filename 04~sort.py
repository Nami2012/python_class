str = input("Enter the list values seperated by space: ")
num_str = (str.split(" "))
num_arr = [int(i) for i in num_str]

arr_len = len(num_arr)

for i in range(arr_len-1):
    for j in range(i+1,arr_len):
        if(num_arr[j]<num_arr[i]):
            temp = num_arr[i]
            num_arr[i] = num_arr[j]
            num_arr[j] = temp

print("The sorted list is: ",num_arr)
