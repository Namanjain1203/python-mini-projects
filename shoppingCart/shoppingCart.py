foods = []
prices = []
total_amt = 0
while True:
    food = input("ENTER FOOD TO BUY(PRESS q TO QUIT) :")
    if food.lower() == "q":
        break
    else: 
        foods.append(food)
        price = int(input(f"ENTER PRICE OF {food} : $"))
        prices.append(price)
print("-YOUR CART-")
for food in foods:
    print(food ,f"${price}")
for price in prices:
    total_amt += price

print(f"TOTAL = ${total_amt}")    