class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    class Point(object):
        def __init__(self, time: int, type: int) -> None:
            self.time = time
            self.type = type

        def __lt__(self, other) -> bool:
            if self.time == other.time:
                return self.type < other.type
            return self.time < other.time

    def countOfAirplanes(self, airplanes: list) -> int:
        points = []
        for a in airplanes:
            points.append(self.Point(a.start, 1))
            points.append(self.Point(a.end, 0))
        points.sort()
        current_count = 0
        max_count = 0
        for p in points:
            if p.type == 1:
                current_count += 1
            else:
                current_count -= 1
            max_count = max(current_count, max_count)
        return max_count
