# Write your solution here
SOUP_PRICE = 5.90
name = input("Please tell me your name:")
if name != "Jerry":
	soup = int(input("How many portions of soup?")) * SOUP_PRICE
	print(f"The total cost is {soup}")
print("Next please!")