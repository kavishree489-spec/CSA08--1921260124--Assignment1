"""
milkrate.py - reusable milk rate and payment functions (Task 7)

Values are calculated with Decimal internally (exact decimal arithmetic) and
returned as floats rounded to 2 decimal places (rupees and paise).
"""
from decimal import Decimal, ROUND_HALF_UP

# ---------- Constants ----------
BASE_RATE = Decimal("30.00")       # Rs per litre at reference quality
BASE_FAT = Decimal("3.5")          # reference fat %
BASE_SNF = Decimal("8.5")          # reference SNF %
STEP_SIZE = Decimal("0.1")         # one step = 0.1 %
FAT_ADJUSTMENT = Decimal("0.40")   # Rs per 0.1 % fat
SNF_ADJUSTMENT = Decimal("0.30")   # Rs per 0.1 % SNF

MIN_FAT, MAX_FAT = 2.0, 7.0        # valid fat range (from the test table)
MIN_SNF, MAX_SNF = 7.0, 10.0       # valid SNF range (assumption)


def _dec(value):
    """Convert to Decimal through str() so 4.2 becomes exactly 4.2."""
    return Decimal(str(value))


def _money(amount):
    """Round a Decimal to 2 places (paise) and return a float."""
    return float(amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def _exact_rate(fat, snf):
    fat_steps = (_dec(fat) - BASE_FAT) / STEP_SIZE
    snf_steps = (_dec(snf) - BASE_SNF) / STEP_SIZE
    return BASE_RATE + fat_steps * FAT_ADJUSTMENT + snf_steps * SNF_ADJUSTMENT


def rate_per_litre(fat, snf):
    """Return the rate per litre for the given fat % and SNF %."""
    return _money(_exact_rate(fat, snf))


def payout(quantity, fat, snf):
    """Return the payment for 'quantity' litres of milk."""
    return _money(_dec(quantity) * _exact_rate(fat, snf))


def valid_input(quantity, fat, snf):
    """True only if quantity > 0 and fat / SNF are inside the allowed ranges."""
    try:
        quantity, fat, snf = float(quantity), float(fat), float(snf)
    except (TypeError, ValueError):
        return False
    if quantity != quantity or fat != fat or snf != snf:   # NaN check
        return False
    return quantity > 0 and MIN_FAT <= fat <= MAX_FAT and MIN_SNF <= snf <= MAX_SNF


def ten_day_total(payments):
    """Return the sum of the daily payments (a list of numbers)."""
    return _money(sum((_dec(p) for p in payments), Decimal("0")))


if __name__ == "__main__":
    # Runs only when this file is executed directly, not when imported.
    print("Milk rate demonstration")
    print(f"{'Litres':>7} {'Fat':>5} {'SNF':>5} {'Rate/L':>9} {'Payment':>10}")
    for litres, fat, snf in [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]:
        print(f"{litres:>7} {fat:>5} {snf:>5} "
              f"{rate_per_litre(fat, snf):>9.2f} {payout(litres, fat, snf):>10.2f}")
