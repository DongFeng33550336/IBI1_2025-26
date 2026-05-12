# Pseudocode for Creatine Clearance Calculator:
# 1. Get input values: age, weight, gender, creatine concentration
# 2. Validate each input against the required ranges:
#    - age must be < 100
#    - weight must be between 20 and 80
#    - creatine must be between 0 and 100
#    - gender must be either 'male' or 'female'
# 3. If any input is invalid, print which variable needs correction
# 4. If all inputs are valid:
#    - Calculate CrCl using Cockcroft-Gault formula
#    - If gender is female, multiply the result by 0.85
#    - Print the calculated Creatine Clearance rate

def calculate_creatine_clearance(age, weight, gender, cr):
    # Input validation
    if age >= 100:
        print("Error: Age must be less than 100 years.")
        return None
    if not (20 < weight < 80):
        print("Error: Weight must be between 20 and 80 kg.")
        return None
    if not (0 < cr < 100):
        print("Error: Creatine concentration must be between 0 and 100 µmol/l.")
        return None
    gender = gender.lower()
    if gender not in ['male', 'female']:
        print("Error: Gender must be either 'male' or 'female'.")
        return None
    
    # Calculate CrCl
    crcl = ((140 - age) * weight) / (72 * cr)
    if gender == 'female':
        crcl = crcl * 0.85
    
    return crcl


# Example usage
if __name__ == "__main__":
    # Test with valid input
    print("Testing valid input (male, 30, 70, 80):")
    result = calculate_creatine_clearance(30, 70, 'male', 80)
    if result:
        print(f"Creatine Clearance: {result:.2f} ml/min")
    
    print("\nTesting invalid input (age 101):")
    result = calculate_creatine_clearance(101, 70, 'male', 80)
    
    print("\nTesting invalid input (weight 90):")
    result = calculate_creatine_clearance(30, 90, 'male', 80)