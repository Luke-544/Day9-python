#2D Lists i python - this is a list of multiple lists

drinks = ["Soda", "Tea", "Juice"]
lunch = ["Rice", "Beef", "Cabbage"]
dessert = ["Ice cream", "Cake"]

food = [drinks, lunch, dessert]
print(food)
print(food[0])
print(food[1][2])

#tuple - similar to lists except they are ordered and unchangeable

student = ("Samuel", 20, "Male")
print(student.count("Samuel"))
print(student.index(20))

for x in student:
    print(x)

if 20 in student:
    print("You are an adult!")