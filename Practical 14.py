phonebook = {}

while True:
    print("\n_______________Phonebook Menu_______________")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Display Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        phonebook[name] = phone
        print("Contact saved!")

    elif choice == "2":
        name = input("Enter name to update: ")

        if name in phonebook:
            phone = input("Enter new phone number: ")
            phonebook[name] = phone
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    elif choice == "3":
        print(phonebook)

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in phonebook:
            del phonebook[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "5":
        print("Thank you for using Phonebook!")
        break

    else:
        print("Invalid choice!")