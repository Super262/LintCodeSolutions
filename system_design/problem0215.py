class Solution:
    def __init__(self):
        self.threshold = {}
        self.hit_timeline = {}

    """
    @param: timestamp: the current timestamp
    @param: event: the string to distinct different event
    @param: rate: the format is [integer]/[s/m/h/d]
    @param: increment: whether we should increase the counter
    @return: true or false to indicate the event is limited or not
    """

    def isRatelimited(self, timestamp: int, event: str, rate: str, increment: bool) -> bool:
        num_str, unit = rate.split("/", 2)
        num = int(num_str)
        if unit == "m":
            self.threshold[event] = (num, 60)
        elif unit == "h":
            self.threshold[event] = (num, 3600)
        elif unit == "d":
            self.threshold[event] = (num, 86400)
        else:
            self.threshold[event] = (num, 1)
        is_limited = self.count_hits(event, timestamp) >= self.threshold[event][0]
        if is_limited:
            return True
        if increment:
            self.hit_timeline[event].append(timestamp)
        return False

    def count_hits(self, event: str, time_span_end: int) -> int:
        if event not in self.hit_timeline:
            self.hit_timeline[event] = []
            return 0
        time_span_start = time_span_end - self.threshold[event][1] + 1
        if time_span_start < 0:
            time_span_start = 0
        first_index_of_start = search_larger_index(self.hit_timeline[event], time_span_start)
        if first_index_of_start == -1:
            return 0
        return len(self.hit_timeline[event]) - first_index_of_start


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
