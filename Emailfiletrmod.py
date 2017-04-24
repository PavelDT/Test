spam_words = ["free", "deal", "$", "offer", "rich", "exclusive", "prize" ] 
# create a list of these words in python3, example email, parsse all the wards in\
#  the example email and check if anything from the list is contained within.
email =  "Greetings reader \
you have been selected as a recipient of a free exclusive offer \
if you would like to know more about the prize you have received \
visit us at this web address" 

email2 = "the meeting tonight will take place in the previously discussed venue"

email3 = "Special offers on sale act now - just click the link!"

email4 = "we have to discuss how we will deal with this situation - contact me asap"
#print the email / do not resassign a string further down the code / changes value\
# current_spam_word is forth with referenced to spam_words = value forth with in the line below
#without changing its value by changing string var
for current_spam_word in spam_words:
    # if current_spam_word in email:
    if email.__contains__(current_spam_word):
        print(" contains spam word: " + current_spam_word)
    else:
        print("this email is not spam")
#creat store in list ( before for loop) 