# Get patient data
age = int(input("Age: "))
weight = float(input("Weight (kg): "))
gender = input("Gender (male/female): ").lower()
cr = float(input("Creatinine (µmol/l): "))

# Validate inputs
msg = ""
if age >= 100:
    msg = "Invalid age: must be < 100"
elif weight <= 20 or weight >= 80:
    msg = "Invalid weight: must be 20–80 kg"
elif cr <= 0 or cr >= 100:
    msg = "Invalid creatinine: must be 0–100 µmol/l"
elif gender not in ["male","female"]:
    msg = "Invalid gender: use male or female"

# Calculate and output
if msg:
    print("Error:", msg)
else:
    crcl = ((140-age)*weight)/(72*cr)
    if gender == "female":
        crcl *= 0.85
    print("CrCl =", round(crcl,2))