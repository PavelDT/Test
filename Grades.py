testresult = int(input("Candidate's score? "))
#invalid input
if testresult > 101 or testresult < 0:
    print("invalid input")
elif testresult >90:
	print("A")
elif testresult > 70:
    print("B")
elif testresult > 50:
	print("C")
elif testresult < 50:
	print("fail")