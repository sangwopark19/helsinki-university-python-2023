# Write your solution he
wage = float(input("Hourly wage:"))
worked = int(input("Hours worked:"))
week = input("Day of the week:")
if week == "Sunday":
	wage *= 2
print(f"Daily wages: {wage * worked} euros")