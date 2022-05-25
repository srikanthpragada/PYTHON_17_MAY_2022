price = int(input("Enter price :"))

if price > 1000:
    discount = price * 0.20
elif price > 500:
    discount = price * 0.10
else:
    discount = price * 0.05

print(f"Selling : {price - discount}")

