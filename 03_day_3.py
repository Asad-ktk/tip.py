# TIP CALCULATOR PROGRAM
total = int(input("Enter total amount of your meal: "))
tip = (total / 100) * 20
person = int(input("Enter number of person's: "))
final = (total + tip) / person
print("Each person will pay: ", final)
