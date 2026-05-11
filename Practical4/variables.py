# 2004 Scotland population
a = 5.08
# 2014 Scotland population
b = 5.33
# 2024 Scotland population
c = 5.55

# 2004-2014 change
d = b - a
# 2014-2024 change
e = c - b

print(f"d={d}")
print(f"e={e}")

# Judge growth trend
if d > e:
    trend = "decelerating"
elif e > d:
    trend = "accelerating"
else:
    trend = "stable"

# Output conclusion
print("Population growth is", trend)

# Boolean variables
X = True
Y = False
W = X or Y
# Print boolean result
print("W =", W)