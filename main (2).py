"""Task 7: using the milkrate module from another script.
Keep milkrate.py and main.py in the same folder."""
import milkrate                       # call as milkrate.payout()
from milkrate import payout          # call as payout()
import milkrate as mr                # call as mr.payout()

print("import milkrate            ->", milkrate.payout(10.5, 4.2, 8.7))
print("from milkrate import payout ->", payout(10.5, 4.2, 8.7))
print("import milkrate as mr      ->", mr.payout(10.5, 4.2, 8.7))
print("Rate per litre (4.2, 8.7)  ->", mr.rate_per_litre(4.2, 8.7))
print("Valid input?  (-5, 3.5, 8.5) ->", mr.valid_input(-5, 3.5, 8.5))

# The demonstration table in milkrate.py does NOT print here
# because __name__ is "milkrate" when imported.
import sys
print("\nmilkrate is cached in sys.modules:", "milkrate" in sys.modules)
print("First entries of sys.path:", sys.path[:2])
