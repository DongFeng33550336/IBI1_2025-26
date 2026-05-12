# Pseudocode for infection simulation:
# 1. Define initial parameters: initial infected, growth rate, total students
# 2. Initialize day counter, start from day 1
# 3. Loop until all students are infected:
#    a. Print current day's infected number
#    b. Update infected number with growth rate
#    c. Increment day counter
# 4. After loop, print total days taken to infect everyone

# Initial parameters
initial_infected = 5
growth_rate = 0.4
total_students = 91

infected = initial_infected
day = 1

print("Infection simulation:")
print(f"Day {day}: {infected} infected")

while infected < total_students:
    # Update infected number
    infected = infected * (1 + growth_rate)
    day += 1
    print(f"Day {day}: {infected} infected")

print(f"\nTotal days to infect all {total_students} students: {day} days")