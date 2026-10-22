"""Intentionally buggy pricing code for an AI code review demo."""

def calculate_total(subtotal, discount_percent=0, tax_rate=0.10):
    """Calculate total after discount and tax."""

    discounted = subtotal * (1 - discount_percent / 100)
    total = discounted * (1 + tax_rate)
    return round(total, 2)
