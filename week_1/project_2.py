#Program to calculate Compound interest
print("Program to calculate Compound interest")


principal = input("Enter the principal amount: ")
rate = input("Enter the rate of interest: ")
time = input("Enter the time period: ")
n = input("Enter the number of times the interest is compounded per year: ")

# Convert inputs to float
principal = float(principal)
rate = float(rate) / 100
time = float(time)
n = float(n)

# Calculate Compound interest
amount = principal * ((1 + rate / n) ** (n * time))
print("The amount after", time, "years is:  {amount:.2f}")