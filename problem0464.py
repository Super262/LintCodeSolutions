class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers2(self, a: list) -> None:
        if not a:
            return
        self.quick_sort(a, 0, len(a) - 1)

    def quick_sort(self, a: list, start: int, end: int) -> None:
        if start >= end:
            return
        pivot = a[start + (end - start) // 2]
        i = start
        j = end
        while i <= j:
            while i <= j and a[i] < pivot:
                i += 1
            while i <= j and a[j] > pivot:
                j -= 1
            if i <= j:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
                i += 1
                j -= 1
        self.quick_sort(a, start, j)
        self.quick_sort(a, i, end)
