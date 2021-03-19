class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """

    def jump(self, a: list) -> int:
        result = 0
        start = 0
        while start < len(a) - 1:
            next_start_choice = range(start + 1, start + a[start] + 1)
            next_start = 0
            max_jump = 0
            for ch in next_start_choice:
                if len(a) - 1 == ch:
                    return result + 1
                jump = ch + a[ch]
                if jump <= max_jump:
                    continue
                next_start = ch
                max_jump = jump
            result += 1
            start = next_start
        return result
