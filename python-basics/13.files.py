with open("profile.txt", "w") as file:
    file.write("Name: Ashish\n")
    file.write("Role: Software Engineer\n")

with open("profile.txt", "r") as file:
    print(file.read())
    print("File read complete.")