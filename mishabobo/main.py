

list_items = ["Apple","Banan","Coconut","Gayfruit"]
list_cost = [10, 12, 20, 50]
a = int(input("0.Apple\n1.Banan\n2.Coconut\n3.Gayfruit\nChoose item:"))
b = int(input("Choose amount:"))

price = b * list_cost[a]

print(f"Price of {b} {list_items[a]} is: {price} ")
c = int(input("How much money u have:"))
if c == price:
    print(f"Thx for purchase!")
elif c < price:
    print("Not enough!\n Purchase canceled!!")
elif c > price:
    print(f"Thx for purchase!")
    print(f"Your remaining is {c-price}")
