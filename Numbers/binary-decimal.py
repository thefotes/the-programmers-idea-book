"""Description: Make a program which has the user enter in either a decimal value and prints out its binary equivalent or enter a binary value and it prints out the decimal equivalent value."""

def to_binary(num):
	num = num
	numc = num
	binary_list = []
	while num > 0:
		binary = num % 2
		binary_list.append(str(binary))
		num = num // 2
	print numc, '=>', " ".join(binary_list[::-1])

nums = raw_input("Enter numbers seperated by a space: ")

for n in nums.split(' '):
	to_binary(int(n))