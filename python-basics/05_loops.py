languages = ["Python", "Kotlin", "Javascript", "Java"]
for lan in languages:
    print(lan)
print("Loop finished.")
for i in range(5):
    print(i)
print("Range loop finished.")

for i in range(2, 10, 2):
    print(i)
print("Step range loop finished.")      
for i in range(10, 0, -1):
    print(i)
print("Reverse range loop finished.")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
print("Nested loop finished.")
for i in range(1, 4):  
    for j in range(1, 4):
        print(f"{i} + {j} = {i+j}")
print("Another nested loop finished.")
             