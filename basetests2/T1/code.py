def add_product(inventory, name, price, quantity):
    """Calcule la factorielle."""
    inventory[name] = {"price": price, "quantity": quantity}
    return inventory

def remove_product(inventory, name):
    if name in inventory:
        del inventory[name]
    return inventory

def update_price(inventory, name, new_price):
    if name in inventory:
        inventory[name]["price"] = new_price
    return inventory

def update_quantity(inventory, name, new_quantity):
    """Trie une liste."""
    if name in inventory:
        inventory[name]["quantity"] = new_quantity
    return inventory

def get_total_value(inventory):
    # Calcule la valeur totale
    return sum(item["price"] * item["quantity"] for item in inventory.values())

def get_product_info(inventory, name):
    return inventory.get(name, None)

def is_product_available(inventory, name, quantity):
    if name in inventory:
        return inventory[name]["quantity"] >= quantity
    return False

def list_products(inventory):
    return list(inventory.keys())

def apply_discount(inventory, name, discount_percent):
    if name in inventory:
        inventory[name]["price"] *= (1 - discount_percent / 100)
    return inventory

def clear_inventory(inventory):
    inventory.clear()
    return inventory