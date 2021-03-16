class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers(self, a: list) -> None:
        if not a:
            return
        a_len = len(a)
        temp = [0] * a_len
        self.merge_sort(a, 0, a_len, temp)

    def merge_sort(self, a: list, start: int, end: int, temp: list) -> None:
        if start >= end - 1:
            return
        mid = start + (end - start) // 2
        self.merge_sort(a, start, mid, temp)
        self.merge_sort(a, mid, end, temp)
        i = start
        j = mid
        temp_p = start
        while i < mid and j < end:
            if a[i] < a[j]:
                temp[temp_p] = a[i]
                i += 1
            else:
                temp[temp_p] = a[j]
                j += 1
            temp_p += 1
        while i < mid:
            temp[temp_p] = a[i]
            i += 1
            temp_p += 1
        while j < end:
            temp[temp_p] = a[j]
            j += 1
            temp_p += 1
        for i in range(start, end):
            a[i] = temp[i]
