#Program to calculate simple interest
print("Program to calculate simple interest")


principal = input("Enter the principal amount: ")
rate = input("Enter the rate of interest: ")
time = input("Enter the time in years: ")

#Convert the inputs to float
principal = float(principal)
rate = float(rate) / 100
time = float(time)

#Simple interest
amount = principal*(1 + (rate/100)*time)
print("The amount after", time, "years is:  {amount:.2f}")


