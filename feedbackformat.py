feedback=input("Enter a feedback: ")

print("\n_____________________________________________________________________________\n")
print("Feedback Format Report".upper().center(80))
print("_____________________________________________________________________________\n")

print("original feedback: ".title().lstrip())
print(feedback)
print("____________________________________________________________________")

print("feedback summary".title())
print("____________________________________________________________________")

print("Total Character Count: ",len(feedback))
print("Total Words Count: ",len(feedback.split()))
print("Total Space Count: ",feedback.count(" "))
print("Total Exclamation Mark Count: ", feedback.count("!"))

print("\n______________________________________________________________________")
print("formated feedback: ".lstrip())
print("________________________________________________________________________\n")

print("Upper case feedbak - ",feedback.upper())
print("Lower case feedback - ",feedback.lower())
print("Title case feedback - ",feedback.title())
print("Capitalise case feedback - ",feedback.capitalize())
print("Swapcase feedback - ",feedback.swapcase())

print("\n")
print("\nProfessional feedback: ".capitalize())

print("word list: ".split())

print("\n____________________________________________________________________\n")
print("thank you for your valuable feedback".upper().center(70))
print("____________________________________________________________________\n")