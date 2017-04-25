spam_words = ["free", "deal", "$", "offer", "rich", "exclusive", "prize"]

emails = ["Greetings reader \
you have been selected as a recipient of a free exclusive offer \
if you would like to know more about the prize you have received \
visit us at this web address", \
          "the meeting tonight will take place in the previously discussed venue", \
          "Special offers on sale act now - just click the link!",\
          "we have to discuss how we will deal with this situation - contact me asap"]

def spam_logic(incoming_email):
    detected_spam = []
    # if current_spam_word in email:
    for current_spam_word in spam_words:
        if current_email.__contains__(current_spam_word):
            detected_spam.append(current_spam_word)  # .lenght or .size
    # a list containing matched spam words for the current email
    if detected_spam.__len__() >= 2:
        print ("this email is spam")
    else:
        print ("this email is clean")

for current_email in emails:
    spam_logic(current_email)
