import random

symbols = ["🍋", "❤️", "⭐", "🍒", "🍇"]

def spin():
    return [random.choice(symbols) for _ in range(3)]

def payout(result, bet):
    if result.count(result[0]) == 3:
        print("🎉 JACKPOT! You won 3x your bet!")
        return bet * 3
    elif result.count(result[0]) == 2 or result.count(result[1]) == 2:
        print("👍 You matched 2 symbols! You won 2x your bet!")
        return bet * 2
    else:
        print("😢 No match. Better luck next time!")
        return 0

def main():
    balance = 500
    print("--------SLOT MACHINE--------")
    print("----------------------------")
    print("SYMBOLS : 🍋 ❤️ ⭐ 🍒 🍇 ")
    print("----------------------------")

    while balance > 0:
        print(f"\nCURRENT BALANCE = ${balance}")
        user_input = input("ENTER BET VALUE (or Q to quit): ")

        if user_input.lower() == 'q':
            print("Thanks for playing!")
            break

        if not user_input.isdigit():
            print("❌ INVALID VALUE. Please enter a number.")
            continue

        bet = int(user_input)

        if bet <= 0:
            print("❌ ENTER A POSITIVE NUMBER")
            continue

        if bet > balance:
            print("❌ INSUFFICIENT BALANCE")
            continue

        balance -= bet

        result = spin()
        print("SPINNING...", " | ".join(result))
        winnings = payout(result, bet)
        balance += winnings

    if balance == 0:
        print("💀 Game Over! You're out of balance.")

if __name__ == '__main__':
    main()
