"""Python code to compute A379726."""
from kings import compute

print("Checking 2")
assert compute(2, 2) == 2
print("Checking 3")
assert compute(3, 2) == 3
print("Checking 4")
assert compute(4, 2) == 8

for n in range(2, 15):
    if n % 3 == 0:
        term = compute(n, 2, best=2 * (n//3)**2 + n//3)
        print(f"{n} {term}")
    else:
        print(f"{n} {2 * ((n+2)//3)**2}")
