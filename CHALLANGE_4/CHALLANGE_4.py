a: int = 12
b: int = 45
c: int = 75

def main():
	global a
	global b
	global c

	print("A:", a)
	print("B:", b)
	print("C:", c)
	
	if a > b and a > c:
		print("MAX:", a)
	elif b > a and b > c:
		print("MAX:", b)
	else:
		print("MAX:", c)
		pass


if __name__ == "__main__":
	main()