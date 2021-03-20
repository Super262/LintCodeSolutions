class Solution:

    def DeleteDigits(self, a: str, k: int) -> str:
        if not a or len(a) <= k:
            return "0"
        deleted_count = 0
        stack = ["\0"] * len(a)
        stack_top = -1
        for digit in a:
            while stack_top >= 0 and deleted_count < k and stack[stack_top] > digit:
                stack_top -= 1
                deleted_count += 1
            if stack_top == -1 and digit == "0":
                continue
            stack_top += 1
            stack[stack_top] = digit
        while deleted_count < k:
            stack_top -= 1
            deleted_count += 1
        if stack_top == -1:
            return "0"
        return "".join(stack[0:stack_top + 1])
