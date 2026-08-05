print("_______________expenses_______________")
expenses=0.0
food=0.0
shopping=0.0
traveling=0.0
other=0.0

while True:
    value=float(input("Enter your amount :"))
    if value == -1:
        break
    category=str(input("enter your category(food/shopping/traveling/other):")).lower()

    if category == "food":
        food += value
    elif category == "shopping":
        shopping += value
    elif category == "traveling":
        traveling += value
    else:
        other += value

    expenses += value


print("\n___________ Expenses Summury ___________")
print("food:", food)
print("shopping:", shopping)
print("traveling:", traveling)
print("other:", other)
print("Total Expenses:", expenses)


