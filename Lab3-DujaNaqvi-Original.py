monthly_fee = 10.0
low_balance_fee = 15.0

current_balance = float(input("Enter the beginning balance: "))
num_checks = int(input("Enter the number of checks written: "))

if current_balance < 0:
    print("URGENT: The account is overdrawn.")

if num_checks < 0:
    print("Error: Number of checks cannot be negative.")
else:
    if num_checks < 20:
        check_rate = 2.5
    elif num_checks <= 39:
        check_rate = 1.5
    elif num_checks <= 59:
        check_rate = 1.0
    else:
        check_rate = 0.5

    check_fees = num_checks * check_rate
    total_fees = monthly_fee + check_fees

    if current_balance < 400:
        total_fees = total_fees + low_balance_fee

    print(f"Total monthly service charges: ${total_fees:.2f}")
