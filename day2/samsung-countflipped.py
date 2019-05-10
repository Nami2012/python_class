"""Given two numbers ‘a’ and b’. Write a program to count number of bits needed to be flipped to convert ‘a’ to ‘b’."""
# Function that count set bits 
def countSetBits( n ): 
	count = 0
	while n: 
		count += n & 1
		n >>= 1
	return count 
	
def FlippedCount(a , b): 
	return countSetBits(a^b) 
 
a = 10
b = 20
print(FlippedCount(a, b)) 

 
