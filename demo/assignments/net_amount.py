# Calculate net amount

price = float(input("Enter price :"))  # str to float
qty = int(input("Enter qty : "))

amount = price * qty
discount = amount * 0.15  # discount at 15%
net_amount = amount - discount

print(f"Amount        {amount:8.2f}")
print(f"- Discount    {discount:8.2f}")
print(f"              {'-' * 8}")
print(f"Net Amount    {net_amount:8.2f}")