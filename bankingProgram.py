def show_balance():
    print(f"BALANCE AMT : $ {balance:.2f}")
def deposit():
    amount = float(input("ENTER AMT TO BE DEPOSITED :"))
    if amount < 0:
        print("INVALID AMT")
        return 0
    else:
        return amount
def withdraw():
    amount = float(input("ENTER WITHDRAWAL AMT :"))
    if amount > balance:
        print("INSUFFICIENT BALANCE")
        return 0
    elif amount<0:
        print("ENTER POSITIVE NUMBER")
    else:
        return amount
balance = 0
running = True
while running:
    print("---BANKING PROGRAM---")
    print("1. BALANCE")
    print("2. DEPOSIT")
    print("3. WITHDRAW")
    print("4. EXIT")

    choice = input("ENTER YOUR CHOICE FROM 1-4: ")
    if choice == "1":
        show_balance()
    elif choice == "2":
        balance+=deposit()
    elif choice == "3":
        balance-=withdraw()
    elif choice == "4":
        running = False

    else:
        print("INVALID CHOICE")

print("THANK YOU")