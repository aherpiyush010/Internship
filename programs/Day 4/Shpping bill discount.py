item=input("Enter the type of item : ")
quantity=int(input("Enter the quantity of item : "))
price=int(input("Enter the price (per item) : "))

total = quantity * price
discount = total-(total*0.10)
final_amount = discount+(discount*0.18)

print("\t ------------- SHOPPING BILL ---------------")
print(f"Item Name : {item}")
print(f"Quantity of item : {quantity}")
print(f"price of item : {price}")
print(f"Total Amount : {total}")
print(f"Total Discount on total price : {discount}")
print(f"gst : {final_amount}")

