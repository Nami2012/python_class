"""Given 3 characters a, b, c. Find the number of strings of length n that can be formed from these 3 characters. 
Given that : we can use ‘a’ as many times as we want, ‘b’ maximum once, and ‘c’ maximum twice."""

for i in range(m):
    n = int(input())
    print((n**3+3*n)//2+1)
