class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """

    def siftup(self, A, k):
        while k != 0:
            father = (k - 1) // 2
            if A[k] > A[father]:
                break
            A[k], A[father] = A[father], A[k]
            k = father

    def heapify(self, A):
        for i in range(len(A)):
            self.siftup(A, i)