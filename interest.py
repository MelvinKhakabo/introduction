#this program calculates simple interest

#input functions
#principal amount
principal_amount = int(input("Enter the principal amount for your item? "))
#rate of interest
rate = int(input("Enter the percentage rate p.a "))
#time in years
time = int(input("Enter the time in years "))

#calculate simple interest
simple_interest = (principal_amount * rate * time) / 100

print(f"The Simple interest is:", simple_interest)