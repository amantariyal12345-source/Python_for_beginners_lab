# Question 8: Store and manage product details using CRUD operations.
products = {}

def add_product():
    product_id = input("Product ID: ").strip()
    if product_id in products:
        print("Product ID already exists.")
        return
    products[product_id] = {
        "name": input("Product name: ").strip(),
        "price": float(input("Price: ")),
        "quantity": int(input("Quantity: ")),
    }
    print("Product added.")

def view_products():
    if not products:
        print("No products found.")
    for product_id, details in products.items():
        print(product_id, details)

def update_product():
    product_id = input("Product ID to update: ").strip()
    if product_id not in products:
        print("Product not found.")
        return
    products[product_id]["name"] = input("New name: ").strip()
    products[product_id]["price"] = float(input("New price: "))
    products[product_id]["quantity"] = int(input("New quantity: "))
    print("Product updated.")

def delete_product():
    product_id = input("Product ID to delete: ").strip()
    if products.pop(product_id, None) is None:
        print("Product not found.")
    else:
        print("Product deleted.")

while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Exit")
    choice = input("Choose: ").strip()
    try:
        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter valid numeric values.")
