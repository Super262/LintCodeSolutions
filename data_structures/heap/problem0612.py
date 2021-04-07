class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """

    def kClosest(self, points: list, origin: Point, k: int) -> list:
        self.quick_select_kth_smallest(origin, points, 0, len(points) - 1, k)
        result = points[0:k]
        result.sort(key=lambda p: (self.get_dis(p, origin), p.x, p.y))
        return result

    def quick_select_kth_smallest(self, origin: Point, points: list, start: int, end: int, k: int) -> int:
        if start >= end:
            return points[start]
        pivot_dis = self.get_dis(points[start + (end - start) // 2], origin)
        i = start
        j = end
        while i <= j:
            while i <= j and self.get_dis(points[i], origin) < pivot_dis:
                i += 1
            while i <= j and self.get_dis(points[j], origin) > pivot_dis:
                j -= 1
            if i <= j:
                points[i], points[j] = points[j], points[i]
                i += 1
                j -= 1
        if start + k - 1 <= j:
            return self.quick_select_kth_smallest(origin, points, start, j, k)
        if start + k - 1 >= i:
            return self.quick_select_kth_smallest(origin, points, i, end, k - (i - start))
        return points[j + 1]

    def get_dis(self, p: Point, origin: Point) -> int:
        return (p.y - origin.y) ** 2 + (p.x - origin.x) ** 2
