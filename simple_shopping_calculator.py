item_1=int(input("Enter price of item 1: "))
quantity_1=int(input("Enter quantity of item 1: "))
item_2=int(input("Enter price of item 2: "))
quantity_2=int(input("Enter quantity of item 2: "))
item_3=int(input("Enter price of item 3: "))
quantity_3=int(input("Enter quantity of item 3: "))

print(f"Item 1: {item_1} x {quantity_1} = {item_1*quantity_1}")
print(f"Item 2: {item_2} x {quantity_2} = {item_2*quantity_2}")
print(f"Item 3: {item_3} x {quantity_3} = {item_3*quantity_3}")
print(f"subtotal: {item_1*quantity_1+item_2*quantity_2+item_3*quantity_3}")
print(f"Tax (8.5%): {(item_1*quantity_1+item_2*quantity_2+item_3*quantity_3)*0.085}")