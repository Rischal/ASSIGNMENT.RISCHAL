price = float(input("Enter the price of the item: "))
if price > 1000:
    new_price = price * 0.80  # Apply 20% discount
    print(f"The new price after 20% discount is: {new_price:.2f}")
elif 500 <= price <= 1000:
    new_price = price * 0.90  # Apply 10% discount
    print(f"The new price after 10% discount is: {new_price:.2f}")
else:
    print("No discount applied. Price remains the same:", price)