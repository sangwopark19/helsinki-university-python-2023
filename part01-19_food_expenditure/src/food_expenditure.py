# Write your solution hear
eat = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
week_money = float(input("How much money do you spend on groceries in a week?"))
week_total = (eat * price) + week_money
day_total = week_total / 7
print("Average food expenditure:")
print(f"Daily: {day_total} euros")
print(f"Weekly: {week_total} euros")