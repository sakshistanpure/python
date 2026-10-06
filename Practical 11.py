bus=[["a","a","a"],
      ["a","a","a"],
      ["a","a","a"],
      ["a","a","a"]]

print("\n")

for i in range (4):
    print(bus[i])
    
print("\n______________Please Reserve Your Seat_____________\n")
row=int(input("Enter Row Number : "))
seat=int(input("Enter Seat number : "))
print("___________________________________")

if bus[row-1][seat-1]=="a":
    bus[row-1][seat-1]="r"
    print("Your Seat Is Reserved.")
    print("___________________________________")
    
else:
    print("Seat Is Already Reserved.")
    
for i in range (4):
    print(bus[i])


    


