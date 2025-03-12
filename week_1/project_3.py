#Program to calculate Annuity plan
print("Program to calculate Annuity plan")

pmt = input("Regular payment made each period: ")
rate = input("Enter the rate of interest: ")
time = input("Enter the time period: ")
n = input("Enter the number of times the interest is compounded per year: ")

# Convert inputs to float
rate = float(rate) / 100
time = float(time)
n = float(n)
pmt = float(pmt)

#Annuity plan
amount = pmt * (((1 + rate/n)**(n * time) - 1) / (rate/n))
print("The amount after", time, "years is: {amount:.2f}")