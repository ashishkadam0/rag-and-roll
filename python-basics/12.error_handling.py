age = input("Enter your age: ")
try:
    age = int(age)
    if age >= 18:
        print("You are an adult.")
    elif age < 0:
        print("Invalid age.")
    else:
        print("You are a minor.")
except ValueError:
    print("Invalid input. Please enter a number.")