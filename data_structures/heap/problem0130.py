class Solution:
    # @param A: Given an integer array
    # @return: void
    def siftdown(self, A, k):
        while k * 2 + 1 < len(A):
            son = k * 2 + 1  # A[i]左儿子的下标
            if k * 2 + 2 < len(A) and A[son] > A[k * 2 + 2]:
                son = k * 2 + 2  # 选择两个儿子中较小的一个
            if A[son] >= A[k]:
                break

            temp = A[son]
            A[son] = A[k]
            A[k] = temp
            k = son

    def heapify(self, A):
        for i in range((len(A) - 1) // 2, -1, -1):
            self.siftdown(A, i)
