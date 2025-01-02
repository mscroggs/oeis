"""Python code to compute A379766."""
from kings import compute

print("Checking 2")
assert compute(2, 4) == 4
print("Checking 3")
assert compute(3, 4) == 9
print("Checking 4")
assert compute(4, 4) == 16

for n in range(2, 15):
    term = compute(n, 4)
    print(f"{n} {term}")
