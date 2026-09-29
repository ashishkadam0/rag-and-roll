import pandas as pd


# A list of dictionaries resembles data returned by many REST APIs.
employees = [
    {"name": "Asha", "team": "AI", "experience_years": 4, "salary": 90000},
    {"name": "Ravi", "team": "Mobile", "experience_years": 6, "salary": 105000},
    {"name": "Neha", "team": "AI", "experience_years": 3, "salary": 85000},
    {"name": "Vikram", "team": "Cloud", "experience_years": 5, "salary": 98000},
]

data_frame = pd.DataFrame(employees)

print("Complete DataFrame:")
print(data_frame)

print("\nFirst two rows:")
print(data_frame.head(2))

print(f"\nShape (rows, columns): {data_frame.shape}")
print(f"Average salary: {data_frame['salary'].mean()}")
print(f"Minimum experience: {data_frame['experience_years'].min()}")
print(f"Maximum experience: {data_frame['experience_years'].max()}")
print(f"Employee count: {data_frame['name'].count()}")

ai_engineers = data_frame[data_frame["team"] == "AI"]
print("\nAI team:")
print(ai_engineers)

first_employee_name = data_frame.loc[0, "name"]
print(f"\nFirst employee: {first_employee_name}")

output_file = "employees.csv"
data_frame.to_csv(output_file, index=False)

loaded_data_frame = pd.read_csv(output_file)
print("\nData loaded from CSV:")
print(loaded_data_frame)

# Exercise:
# Filter employees with at least five years of experience, then print their
# names and the average salary of the filtered rows.
