score = 0

def mark_grade(testresult):
    feedback_message = "error in processesing grade"
    #invalid input
    if testresult > 101 or testresult < 0:
        print("invalid input")
        feedback_message = "excellent work"
    elif testresult >90:
        print("A")
        feedback_message = "excellent work"
    elif testresult > 70:
        print("B")
        feedback_message = "excellent work"
    elif testresult > 50:
        print("C")
        feedback_message = "good work"
    elif testresult < 50:
        print("fail")
        feedback_message = "needs improvement"
    
    return feedback_message

#function chaining - func within parenthesis
while(score > 0 and score < 100)
	score = int(input("Candidate's score? "))
	print(mark_grade(score))

# variable
# function_with_no_params()
# function_with_1_param(variable_here)
# function_with_2_parameters(variable_here_1, 77)
