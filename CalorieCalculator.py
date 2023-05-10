print("Welcome to the Calorie Calculator")

nutrients = ["carbohydrates", "proteins", "fats"]
amounts = []

for nutrient in nutrients:
    while True:
        try:
            input_str = input(f"Enter the amount and unit of measurement for {nutrient} (e.g. 100 g, 3 oz): ")
            amount, unit = input_str.split(" ")
            amount = float(amount)
            break
        except ValueError:
            print("Invalid input. Please enter a number followed by a unit of measurement (e.g. 100 g, 3 oz)")


    if unit == "oz":
        amount *= 28.35  # 1 oz = 28.35 g
    amounts.append(amount)

# Calculate the total number of calories
calories = (amounts[0] * 4) + (amounts[1] * 4) + (amounts[2] * 9)

# Display the result to the user
print("This food contains about ", calories, "calories")

