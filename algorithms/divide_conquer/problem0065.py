class Solution:

    def findMedianSortedArrays(self, A: list, B: list) -> float:
        n = len(A) + len(B)
        if n % 2 == 0:
            return (self.find_kth(A, 0, B, 0, n // 2) + self.find_kth(A, 0, B, 0, n // 2 + 1)) / 2.0
        else:
            return self.find_kth(A, 0, B, 0, n // 2 + 1)

    def find_kth(self, a: list, start_a: int, b: list, start_b: int, k: int) -> int:
        if start_a >= len(a):
            return b[start_b + k - 1]
        if start_b >= len(b):
            return a[start_a + k - 1]
        if k == 1:
            # k = 1 时，我们需要特殊处理，因为我们无法对 k 进行合法分割
            return min(a[start_a], b[start_b])
        if start_a + k // 2 - 1 > len(a):
            half_k_of_a = 2147483647
        else:
            half_k_of_a = a[start_a + k // 2 - 1]
        if start_b + k // 2 - 1 > len(b):
            half_k_of_b = 2147483647
        else:
            half_k_of_b = b[start_b + k // 2 - 1]
        if half_k_of_a < half_k_of_b:
            return self.find_kth(a, start_a + k // 2, b, start_b, k - k // 2)
        else:
            return self.find_kth(a, start_a, b, start_b + k // 2, k - k // 2)
