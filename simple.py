def calculate_simple_interest(principal, annual_rate, years):
    interest = (principal * annual_rate * years) / 100
    total_amount = principal + interest

    return interest, total_amount

interest, total_amount = calculate_simple_interest(10000, 5, 2)

print(f"Final Amount: ${interest:.2f}")
print(f"Simple Interest Earned: ${total_amount:.2f}")

def calculate_compound_interest(principal, annual_rate, compounds_per_year, years):
    rate = annual_rate / 100
    final_amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)
    interest = final_amount - principal

    return final_amount, interest


final_amount, interest = calculate_compound_interest(10000, 8, 4, 5)

print(f"Final Amount: ₹{final_amount:.2f}")
print(f"Interest Earned: ₹{interest:.2f}")



