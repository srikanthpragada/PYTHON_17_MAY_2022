# Calculate net amount

price = float(input("Enter price :"))  # str to float
qty = int(input("Enter qty : "))

amount = price * qty
discount = amount * 0.15  # discount at 15%

net_amount = amount - discount
print("Net Amount = ", net_amount)
