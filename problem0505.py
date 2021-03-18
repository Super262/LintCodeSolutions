class WebLogger:

    def __init__(self):
        self.timeline = []

    """
    @param: timestamp: An integer
    @return: nothing
    """

    def hit(self, timestamp):
        self.timeline.append(timestamp)

    """
    @param: timestamp: An integer
    @return: An integer
    """

    def get_hit_count_in_last_5_minutes(self, timestamp):
        time_span_start = timestamp - 300 + 1
        if time_span_start < 0:
            time_span_start = 0
        first_index_of_start = search_larger_index(self.timeline, time_span_start)
        if first_index_of_start == -1:
            return 0
        return len(self.timeline) - first_index_of_start


def search_larger_index(array: list, target: int) -> int:
    if not array:
        return -1
    start = 0
    end = len(array) - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        if array[mid] >= target:
            end = mid
        else:
            start = mid + 1
    if array[start] >= target:
        return start
    if array[end] >= target:
        return end
    return -1
