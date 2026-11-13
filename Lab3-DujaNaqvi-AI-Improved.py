# Lab 3: Branches and Decision-Making
# AI-Improved Version

monthly_fee = 10.0
low_balance_fee = 15.0

# Get user input
current_balance = float(input("Enter the beginning balance: "))
num_checks = int(input("Enter the number of checks written: "))

# Check for an overdrawn account
if current_balance < 0:
    print("URGENT: The account is overdrawn.")

# Validate number of checks
if num_checks < 0:
    print("Error: Number of checks cannot be negative.")

else:
    # Determine the fee per check
    if num_checks < 20:
        check_rate = 2.50
    elif num_checks < 40:
        check_rate = 1.50
    elif num_checks < 60:
        check_rate = 1.00
    else:
        check_rate = 0.50

    # Calculate check fees
    check_fees = num_checks * check_rate

    # Calculate total monthly fees
    total_fees = monthly_fee + check_fees

    # Apply low balance fee if necessary
    if current_balance < 400:
        total_fees += low_balance_fee

    # Display final result
    print(f"Total monthly service charges: ${total_fees:.2f}")
