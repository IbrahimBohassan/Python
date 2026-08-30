app_name = "Math Utility"
data_points = [10, 20, 30, 40, 50]

def calculate_average(numbers):
    return sum(numbers) / len(numbers)
result = calculate_average(data_points)
print(f"Script executed! Deafult average: {result}")