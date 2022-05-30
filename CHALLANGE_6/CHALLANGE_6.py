a: int = 12
b: int = 45
oper: str = "+"

def calculate(left: int, right: int, operation: str):
	if operation == '+':
		return left + right
	if operation == '-':
		return left - right
	if operation == '*':
		return left * right
	if operation == '/':
		return left / right
	pass


def main():
	global a
	global b
	global oper

	print("A: {0}".format(a))
	print("B: {0}".format(b))
	print("OPERATION: {0}".format(oper))
	print()

	result = calculate(a, b, oper)
	if result is not None:
		print("RESULT: {0}".format(result))
	else:
		print("Cannot calculate RESULT")
	pass

if __name__ == "__main__":
	main()