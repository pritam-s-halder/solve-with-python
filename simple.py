# def calculate_compound_interest():
#     principal_amount = float(input("Enter amount: "))
#     annual_rate = float(input("Enter rate: "))
#     compounds_per_year = int(input("Enter compounding periods per year: "))
#     years = int(input("Enter no. of years: "))
#
#     rate = annual_rate / 100
#
#     final_amount = principal_amount * (1 + rate / compounds_per_year) ** (compounds_per_year * years)
#     interest_earned = final_amount - principal_amount
#
#     print(f"\nFinal Amount: {final_amount}")
#     print(f"Compound Interest Earned: {interest_earned:.2f}")
#
# calculate_compound_interest()

def calculate_simple_interest(principal, annual_rate, years):
    interest = (principal * annual_rate * years) / 100
    total_amount = principal + interest

    return interest, total_amount

interest, total_amount = calculate_simple_interest(10000, 5, 2)

print(f"Final Amount: ${interest:.2f}")
print(f"Simple Interest Earned: ${total_amount:.2f}")



