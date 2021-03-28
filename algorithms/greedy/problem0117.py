class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """

    def jump(self, a: list) -> int:
        result = 0
        first_start = 0
        while first_start < len(a) - 1:
            next_start_choices = range(first_start + 1, first_start + a[first_start] + 1)
            next_start = 0
            max_jump = 0
            for ch in next_start_choices:
                if len(a) - 1 == ch:
                    return result + 1
                jump = ch + a[ch]
                if jump <= max_jump:
                    continue
                next_start = ch
                max_jump = jump
            result += 1
            first_start = next_start
        return result
