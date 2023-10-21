# Write your solution herestudents
students = int(input("How many students on the course?"))
size = int(input("Desired group size?"))
group = students // size
if students % size > 0:
	group += 1
print(f"Number of groups formed: {group}")