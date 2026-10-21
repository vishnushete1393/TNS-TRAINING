# Raw stock delivery data
raw_delivery = [
    ("Apple", 0.75, 50),
    ("Banana", 0.40, 100),
    ("Milk", 2.50, 15),
    ("Bread", 1.80, 20),
    ("Apple", 0.75, 30),  # Extra stock of apples arriving
]

# Customer shopping cart
shopping_cart = ["Apple", "Apple", "Milk", "Dragonfruit", "Bread"]


def inventory(raw_delivery):
    inventory = {}

    for product_name, price, quantity in raw_delivery:
        if product_name in inventory:
            inventory[product_name]["stock"] += quantity
        else:
            inventory[product_name] = {
                "price": price,
                "stock": quantity
            }

    return inventory


def process_checkout(cart, inventory):
    receipt = []
    total = 0.0

    for item in cart:
        if item not in inventory:
            print(f"{item} is sold out!")
        elif inventory[item]["stock"] <= 0:
            print(f"{item} is sold out!")
        else:
            price = inventory[item]["price"]

            receipt.append((item, price))
            total += price

            # Reduce stock by 1
            inventory[item]["stock"] -= 1

    return receipt, total


# Create inventory
store_inventory = inventory(raw_delivery)

# Process checkout
receipt, total_price = process_checkout(
    shopping_cart,
    store_inventory
)

# Print Receipt
print("\n--- CUSTOMER RECEIPT ---")

for product, price in receipt:
    print(f"{product}: ${price:.2f}")

print("-" * 24)
print(f"TOTAL: ${total_price:.2f}")
print("-" * 24)

print("\nRemaining Inventory:", store_inventory)
