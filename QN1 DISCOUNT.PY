price = float(input("Enter the price of the item: "))

if price > 1000:
    discount = 0.10
elif price > 500:
    discount = 0.05
else:
    discount = 0

final_price = price * (1 - discount)

print(f"The final price after discount is: {final_price:.2f}")