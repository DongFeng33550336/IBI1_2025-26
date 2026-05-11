class food_item:
    """
    Class to store nutrition information of a single food item
    """
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein  # Unit: gram
        self.carbs = carbs      # Unit: gram
        self.fat = fat          # Unit: gram


def calculate_daily_nutrition(food_list):
    """
    Calculate total nutrition intake for a day, and check for warnings
    :param food_list: List of food_item instances consumed in 24 hours
    """
    total_calories = 0.0
    total_protein = 0.0
    total_carbs = 0.0
    total_fat = 0.0

    # Sum up all nutrition data
    for food in food_list:
        total_calories += food.calories
        total_protein += food.protein
        total_carbs += food.carbs
        total_fat += food.fat

    # Print summary
    print("Daily Nutrition Intake Summary")
    print(f"Total Calories: {total_calories:.1f} kcal")
    print(f"Total Protein:  {total_protein:.1f} g")
    print(f"Total Carbs:    {total_carbs:.1f} g")
    print(f"Total Fat:      {total_fat:.1f} g")

    # Check warning thresholds
    print("\nWarning Check")
    has_warning = False
    if total_calories > 2500:
        print("WARNING: Exceeded daily calorie limit (2500 kcal)!")
        has_warning = True
    if total_fat > 90:
        print("WARNING: Exceeded daily fat limit (90 g)!")
        has_warning = True
    if not has_warning:
        print("No warnings, your intake is within normal range.")


if __name__ == "__main__":
    # Example 1: Normal daily intake
    print("Example 1: Normal daily intake test")
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    chicken_breast = food_item("Chicken Breast", 165, 31, 3.6, 3.6)
    steamed_rice = food_item("Steamed Rice", 130, 2.7, 28, 0.3)
    broccoli = food_item("Broccoli", 55, 3.7, 11, 0.6)

    normal_diet = [apple, chicken_breast, steamed_rice, broccoli]
    calculate_daily_nutrition(normal_diet)

    # Example 2: Excessive intake to test warning function
    print("\n\nExample 2: Excessive intake test (warning demo)")
    cheeseburger = food_item("Cheeseburger", 303, 15, 24, 18)
    fries = food_item("French Fries", 365, 4, 48, 17)
    cola = food_item("Cola", 140, 0, 39, 0)
    pizza = food_item("Pepperoni Pizza", 298, 12, 34, 14)
    ice_cream = food_item("Ice Cream", 270, 5, 31, 15)

    excessive_diet = [cheeseburger, fries, cola, pizza, ice_cream, cheeseburger, fries]
    calculate_daily_nutrition(excessive_diet)