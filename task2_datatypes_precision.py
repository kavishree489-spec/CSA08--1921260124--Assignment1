"""Task 2: Data types, operators and floating-point precision"""
from decimal import Decimal
import time

print("1. Arithmetic operations")
print("Division           7 / 2      =", 7 / 2)
print("Floor division     7 // 2     =", 7 // 2)
print("Modulus            7 % 2      =", 7 % 2)
print("Unary + floor div  -(-7) // 2 =", -(-7) // 2)

print("\n2. Floating-point precision")
print("0.1 + 0.2          =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3   ->", 0.1 + 0.2 == 0.3)
print("Decimal('0.1') + Decimal('0.2')            =", Decimal("0.1") + Decimal("0.2"))
print("Decimal('0.1') + Decimal('0.2') == Decimal('0.3') ->",
      Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

print("\n3. Money calculation comparison (Rs 10.50 x 3 litres)")
# Float method
float_total = 10.50 * 3
print("Float method      :", float_total)
# Decimal method (created from strings)
decimal_total = Decimal("10.50") * 3
print("Decimal method    :", decimal_total)
# Integer paise method (Rs 10.50 = 1050 paise)
paise_total = 1050 * 3
print("Integer paise     :", paise_total, "paise = Rs", paise_total // 100, "and",
      paise_total % 100, "paise")

# Where float error becomes visible
print("\nFloat error example: sum of 0.10 added 10 times")
f = 0.0
d = Decimal("0")
p = 0
for _ in range(10):
    f += 0.10
    d += Decimal("0.10")
    p += 10
print("Float   :", f, "(== 1.0 ?", f == 1.0, ")")
print("Decimal :", d, "(== 1.0 ?", d == Decimal('1.0'), ")")
print("Paise   :", p, "paise (== 100 ?", p == 100, ")")

print("\n4. Complexity analysis - total of N payments")
N = 100000
payments = [Decimal("33.40")] * N
start = time.perf_counter()
total = Decimal("0")
for pay in payments:            # one pass over N records -> O(N) time
    total += pay                # only one variable besides the list -> O(1) auxiliary space
print(f"Total of {N} payments = {total}  (time {time.perf_counter() - start:.4f} s)")
print("Time complexity = O(N); auxiliary space = O(1) (the list itself is O(N)).")
