"""Intentionally buggy pricing code for an AI code review demo."""

def calculate_total(subtotal, discount_percent=0, tax_rate=0.10):
    """Calculate total after discount and tax."""
    if subtotal < 0:
        raise ValueError("subtotal must be non-negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")
    if not 0 <= tax_rate <= 1:
        raise ValueError("tax_rate must be between 0 and 1")

    discounted = subtotal * (1 - discount_percent / 100)
    total = discounted * (1 + tax_rate)
    return round(total, 2)
