str = input("Enter a string: ")
sub = input("Enter the substring: ")

str_len = len(str)
sub_len = len(sub)

count = 0

for i in range(str_len):
    if(str[i]==sub[0]):
        if(str[i:i+sub_len]==sub):
            count+=1

print("Count is ",count)