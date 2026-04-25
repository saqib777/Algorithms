# Algorithm: Greedy (Sort by Value/Weight Ratio)
# Time Complexity:  O(n log n) — dominated by sorting
# Space Complexity: O(1)       — in-place sorting

def fractional_knapsack(capacity: int, items: list[tuple[int, int]]) -> float:
    """
    Maximise total value in a knapsack of given capacity.
    Unlike 0/1 knapsack, fractions of items are allowed.

    Each item is (weight, value).

    Greedy insight: sort by value-per-unit-weight (density)
    descending. Take as much of the highest-density item
    as possible before moving to the next.

    This greedy works for fractional knapsack but NOT for
    0/1 knapsack (where DP is required).
    """
    # Sort by value/weight ratio descending
    sorted_items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)

    total_value    = 0.0
    remaining_cap  = capacity

    for weight, value in sorted_items:
        if remaining_cap <= 0:
            break
        if weight <= remaining_cap:
            # Take the whole item
            total_value   += value
            remaining_cap -= weight
        else:
            # Take a fraction
            fraction        = remaining_cap / weight
            total_value    += value * fraction
            remaining_cap   = 0

    return round(total_value, 4)


def fractional_knapsack_with_trace(capacity: int, items: list[tuple[int,int]]) -> dict:
    """
    Same algorithm but returns a full trace of selections
    for debugging and educational purposes.
    """
    sorted_items = sorted(
        enumerate(items), key=lambda x: x[1][1]/x[1][0], reverse=True
    )
    total_value   = 0.0
    remaining_cap = capacity
    selections    = []

    for orig_idx, (weight, value) in sorted_items:
        if remaining_cap <= 0:
            break
        if weight <= remaining_cap:
            fraction = 1.0
        else:
            fraction = remaining_cap / weight

        taken = weight * fraction
        gained = value * fraction
        total_value   += gained
        remaining_cap -= taken

        selections.append({
            'item': orig_idx,
            'weight': weight,
            'value': value,
            'fraction_taken': round(fraction, 4),
            'value_gained': round(gained, 4),
        })

    return {'max_value': round(total_value, 4), 'selections': selections}


if __name__ == "__main__":
    items = [(10, 60), (20, 100), (30, 120)]
    print(fractional_knapsack(50, items))   # 240.0

    items2 = [(2, 10), (3, 5), (5, 15), (7, 7), (1, 6), (4, 18), (1, 3)]
    print(fractional_knapsack(15, items2))  # 55.3333...

    trace = fractional_knapsack_with_trace(50, items)
    for s in trace['selections']:
        print(s)
