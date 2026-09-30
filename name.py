# code for  cloud kitchen
print("welcome to cloud kitchen")
print("we have following itmes in cloud kitchan")
print(
"press 1 for  paratha ₹40/2piece",
"press 2 for mango juice ₹50/per glass",
"press 3 for rajma chawal ₹70/per piece",
"press 4 for noodles ₹60/per plate .")
print("choose from the above list and press the number")
item=int(input("enter your choose number"))
quantity=float(input("enter your quantity of item"))
if item==1:
    price= 40*quantity
    print(price)
elif item==2:
    price= 50*quantity
    print(price)
elif item==3:
    price= 70*quantity
    print(price)
elif item==4:
    price= 60*quantity
    print(price)
else:
    print("we are really sorry this item is not available")
