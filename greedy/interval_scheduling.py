# Algorithm: Greedy — Sort by End Time (for max intervals)
#            Greedy — Sort by Start Time + Min-Heap (for min rooms)
# Time Complexity:  O(n log n)
# Space Complexity: O(n)

import heapq


def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    """
    Return the minimum number of intervals to remove so that
    the remaining intervals do not overlap.

    Equivalent to: n - max_non_overlapping_intervals.

    Greedy: sort by end time. Greedily keep intervals that
    end earliest — they leave the most room for others.
    Count how many we must remove (those that overlap the last kept).
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])
    last_end = intervals[0][1]
    removed  = 0

    for start, end in intervals[1:]:
        if start < last_end:
            removed += 1          # overlaps — remove current
        else:
            last_end = end        # no overlap — keep it, update boundary

    return removed


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    """
    Return the minimum number of conference rooms required
    to hold all meetings without conflict.

    Greedy + Min-Heap:
    Sort meetings by start time. For each meeting, if the
    earliest-ending room is free, reuse it. Otherwise add a room.
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    heap = []  # stores end times of ongoing meetings

    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)
        else:
            heapq.heappush(heap, end)

    return len(heap)


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Merge all overlapping intervals and return the result.

    Sort by start time. For each interval, if it overlaps
    the last merged interval, extend it. Otherwise append.
    """
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


if __name__ == "__main__":
    print(erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]))  # 1
    print(erase_overlap_intervals([[1,2],[1,2],[1,2]]))        # 2
    print(erase_overlap_intervals([[1,2],[2,3]]))              # 0

    print(min_meeting_rooms([[0,30],[5,10],[15,20]]))          # 2
    print(min_meeting_rooms([[7,10],[2,4]]))                   # 1

    print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))        # [[1,6],[8,10],[15,18]]
    print(merge_intervals([[1,4],[4,5]]))                       # [[1,5]]
