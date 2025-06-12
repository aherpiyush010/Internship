# Shopping bill
item=input("Enter the type of item : ")
quantity=int(input("Enter the quantity of item : "))
price=int(input("Enter the price (per item) : "))

total = quantity * price

print("\t ------------- SHOPPING BILL ---------------")
print("item\t      Quantity\t  price(per item )\t  total")
print(f"{item}\t\t{quantity}\t\t{price}\t\t  {total}")