try:
    print("Inside try")
except NameError:
    print("Found error")
else:
	print("else block")
finally:
	print("Finally block")