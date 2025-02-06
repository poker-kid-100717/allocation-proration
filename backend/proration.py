from typing import List, Dict
from models import Investor  # Import Investor from models.py

def prorate_allocation(allocation_amount: float, investor_amounts: List[Dict]) -> Dict:
    """
    Prorates the allocation amount based on investors' average investment amounts.
    Ensures no one gets more than their requested amount.
    """
    # Calculate total historical average sum
    total_avg = sum(inv.average_amount for inv in investor_amounts)  # Correct access

    # First pass: Initial proration
    allocated = {
        inv.name: min(inv.requested_amount, allocation_amount * (inv.average_amount / total_avg))
        for inv in investor_amounts  # Correct access to object attributes
    }

    # Calculate remaining allocation after the first pass
    used_allocation = sum(allocated.values())
    remaining_allocation = allocation_amount - used_allocation

    # Second pass: Redistribute unused funds (if any)
    while remaining_allocation > 0:
        eligible_investors = [
            inv for inv in investor_amounts
            if allocated[inv.name] < inv.requested_amount
        ]

        if not eligible_investors:
            break  # No more investors can receive extra funds

        total_avg_remaining = sum(inv.average_amount for inv in eligible_investors)  # Correct access

        for inv in eligible_investors:
            # Ensure we do not allocate more than the requested amount
            additional_amount = min(
                inv.requested_amount - allocated[inv.name],
                remaining_allocation * (inv.average_amount / total_avg_remaining)
            )
            allocated[inv.name] += additional_amount

        # Recalculate remaining allocation
        used_allocation = sum(allocated.values())
        remaining_allocation = allocation_amount - used_allocation

    return allocated

