#program that calculates your discounted price
#input original price
price = int(input("Please input the original price of the item "))

# input discount percentage
discount = int(input("Input a percentage discount "))

#calculate discounted price
discounted_price = price * (100 - discount) / 100

print(f"The discounted price is:", discounted_price)