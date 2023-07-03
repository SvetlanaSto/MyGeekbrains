MULT = 50
PERCENT = 0.015
EXTRA_PERCENT = 0.03
RICH_PERCENT = 0.1
MIN_CASH = 30
MAX_CASH = 600
MAX_COUNT = 3
MAX_SCORE = 5_000_000


def calculate_withdrawal_fee(amount):
    fee = amount * PERCENT
    fee = max(fee, MIN_CASH)
    fee = min(fee, MAX_CASH)
    return fee


def calculate_interest(amount, count):
    if count % MAX_COUNT == 0:
        interest = amount * EXTRA_PERCENT
        print("Начислены проценты: ", interest)
        return interest
    else:
        return 0


def calculate_wealth_tax(amount):
    if amount > MAX_SCORE:
        tax = amount * RICH_PERCENT
        return tax
    else:
        return 0


def main():
    total_score = 0
    count = 0

    while True:
        print("Текущий баланс: ", total_score)
        action = input("Введите действие (пополнить, снять, выйти): ")

        if action == "пополнить":
            deposit_amount = int(input("Введите сумму пополнения (кратную 50): "))
            if deposit_amount % MULT != 0:
                print("Сумма пополнения должна быть кратной 50!")
                continue

            total_score += deposit_amount
            count += 1
            total_score += calculate_interest(total_score, count)
            total_score -= calculate_wealth_tax(total_score)

        elif action == "снять":
            withdrawal_amount = int(input("Введите сумму снятия (кратную 50): "))
            if withdrawal_amount % MULT != 0:
                print("Сумма снятия должна быть кратной 50!")
                continue

            if withdrawal_amount > total_score:
                print("Недостаточно средств на счете!")
                continue

            fee = calculate_withdrawal_fee(withdrawal_amount)
            total_score -= withdrawal_amount + fee
            count += 1
            total_score += calculate_interest(total_score, count)
            total_score -= calculate_wealth_tax(total_score)

        elif action == "выйти":
            break

        else:
            print("Неверное действие! Попробуйте еще раз.")


main()

