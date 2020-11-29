import random
import string

n = int(input("Enter the length of the password : "))

def generate(n):
	password = ''
	for i in range(n):
		password += random.choice(string.ascii_letters)
		password += str(random.randint(0, 10))
		if len(password) == n:
			break
		else:
			continue
	return password

print(generate(n))