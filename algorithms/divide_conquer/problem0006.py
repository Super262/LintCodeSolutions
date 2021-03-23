class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, a: list, b: list) -> list:
        a_len = len(a)
        b_len = len(b)
        result = [0] * (a_len + b_len)
        result_p = 0
        a_p = 0
        b_p = 0
        while a_p < a_len and b_p < b_len:
            if a[a_p] < b[b_p]:
                result[result_p] = a[a_p]
                a_p += 1
            else:
                result[result_p] = b[b_p]
                b_p += 1
            result_p += 1
        while a_p < a_len:
            result[result_p] = a[a_p]
            a_p += 1
            result_p += 1
        while b_p < b_len:
            result[result_p] = b[b_p]
            b_p += 1
            result_p += 1
        return result
