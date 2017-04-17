n = 100
total_sum = 0
counter = 1

def add_total_up(some_number):
    global total_sum 
    total_sum = total_sum + some_number
    print("total sum sofar " + str(total_sum))

#global scope indentation defines local variables 
#(how something is defined and what the function does)
while counter <= n:
    counter += 1
    print(counter)
    add_total_up(counter)

#add_total_up(3)
print("Count of loops: " + str(n) + "\nTotal sum: "  + str(total_sum))
#\n new line break in strings

