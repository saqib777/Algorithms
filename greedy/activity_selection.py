# Algorithm: Greedy (Sort by Finish Time)
# Time Complexity:  O(n log n) — dominated by sorting
# Space Complexity: O(n)       — result list

def activity_selection(activities: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Select the maximum number of non-overlapping activities.

    Each activity is (start_time, finish_time).
    Two activities overlap if one starts before the other finishes.

    Greedy insight: always pick the activity that finishes earliest
    — it leaves the most time for remaining activities.

    Classic scheduling problem. Used in:
    interval scheduling, meeting rooms, CPU task scheduling.

    Example:
        activities = [(1,4),(3,5),(0,6),(5,7),(3,8),(5,9),(6,10),(8,11),(8,12),(2,13),(12,14)]
        Output: [(1,4),(5,7),(8,11),(12,14)]
    """
    if not activities:
        return []

    sorted_acts = sorted(activities, key=lambda x: x[1])
    selected    = [sorted_acts[0]]

    for start, finish in sorted_acts[1:]:
        if start >= selected[-1][1]:
            selected.append((start, finish))

    return selected


def count_meetings(rooms: list[tuple[int, int]]) -> int:
    """
    Variant: minimum meeting rooms needed to hold all meetings.
    Uses a greedy approach with a min-heap tracking room end times.
    Time: O(n log n)
    """
    import heapq
    if not rooms:
        return 0

    sorted_rooms = sorted(rooms, key=lambda x: x[0])
    heap = []

    for start, end in sorted_rooms:
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)
        else:
            heapq.heappush(heap, end)

    return len(heap)


if __name__ == "__main__":
    acts = [(1,4),(3,5),(0,6),(5,7),(3,8),(5,9),(6,10),(8,11),(8,12),(2,13),(12,14)]
    print(activity_selection(acts))  # [(1,4),(5,7),(8,11),(12,14)]

    meetings = [(0,30),(5,10),(15,20)]
    print(count_meetings(meetings))  # 2
