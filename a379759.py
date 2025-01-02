"""Python code to compute A379759."""
from kings import compute

print("Checking 2")
assert compute(2, 3) == 3
print("Checking 3")
assert compute(3, 3) == 5
print("Checking 4")
assert compute(4, 3) == 12

for n in range(2, 15):
    term = compute(n, 3)
    print(f"{n} {term}")
