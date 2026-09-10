inventory = ["Laptop","Smartphone","Headphones","Keyboard","Mouse","Monitor"]
print("________________________________________")
print("Current Inventory:")
print("________________________________________")
for index, item in enumerate(inventory):
    print(f"{index}: {item}")

item_name = input("\nEnter the item you want to search for: ").strip()
print("________________________________________")

if item_name in inventory:
    index = inventory.index(item_name)
    print(f"\n✓ '{item_name}' is present in the inventory.")
    print("________________________________________\n")
    print(f"Index position: {index}")
    print("\n")
else:
    print(f"\n✗ '{item_name}' was not found in the inventory.")
