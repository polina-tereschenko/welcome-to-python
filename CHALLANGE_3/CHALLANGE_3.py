a: int = 12
b: int = 45

def main():
	global a
	global b
	if a < b:
		print("A < B")
	# elif a > b:
	# 	print("A > B")
	else:
		print("A == B")
pass


if __name__ == "__main__":
	main()