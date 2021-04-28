class Solution:

    def rerange(self, A: list) -> None:
        if not A:
            return
        i = 0
        j = len(A) - 1
        while i <= j:
            while i <= j and A[i] < 0:
                i += 1
            while i <= j and A[j] > 0:
                j -= 1
            if i <= j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        # Notice that the quantity of positive numbers may not equal to the quantity of negative numbers
        count_positive = 0
        for num in A:
            if num > 0:
                count_positive += 1
        count_negative = len(A) - count_positive
        if count_negative > count_positive:
            i = 1
            j = len(A) - 1
        elif count_negative < count_positive:
            i = 0
            j = len(A) - 2
        else:
            i = 0
            j = len(A) - 1
        while i <= j and A[i] < 0 and A[j] > 0:
            A[i], A[j] = A[j], A[i]
            i += 2
            j -= 2
