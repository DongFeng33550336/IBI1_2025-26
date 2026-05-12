# Population data for Scotland
a = 5.08  # Population in 2004 (million)
b = 5.33  # Population in 2014 (million)
c = 5.55  # Population in 2024 (million)

# Calculate population changes
d = b - a  # Change between 2004 and 2014
e = c - b  # Change between 2014 and 2024

# Compare d and e
print(f"Population change 2004-2014: {d} million")
print(f"Population change 2014-2024: {e} million")
# Comment: d is larger than e, so population growth in Scotland is decelerating.

# Boolean variables part
X = True
Y = False
W = X or Y

# Truth table for W = X or Y
# X     | Y     | W (X or Y)
# True  | True  | True
# True  | False | True
# False | True  | True
# False | False | False