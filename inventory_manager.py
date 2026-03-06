import json

# Task 1 — Read the inventory

with open("inventory.json", "r") as file:
    inventory = json.load(file)

print(f"Total books in inventory: {len(inventory)}")


# Task 2 — Update and save

new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

inventory.append(new_book)

with open("inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)

print("Inventory updated and saved successfully.")

# Task 3 — Display the inventory
with open("inventory.json", "r") as file:
    updated_inventory = json.load(file)

print("\n--- Bookstore Inventory ---")
for book in updated_inventory:
    print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']:.2f}")