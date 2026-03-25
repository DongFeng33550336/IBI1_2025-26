# Infection Spread Simulation
# Total students
total = 91

# Initial infected people
infected = 5

# Daily infection rate
rate = 0.4

# Day counter
day = 0

# Calculate infection spread each day
while infected < total:
    day = day + 1
    infected = infected * (1 + rate)

    if infected > total:
        infected = total

    print("Day", day, ":", infected, "infected")

# Show total days
print("All infected after", day, "days")