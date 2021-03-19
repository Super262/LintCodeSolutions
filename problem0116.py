class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """

    def canJump(self, a: list) -> bool:
        if not list:
            return False
        last_index = len(a) - 1
        global_limit = 0
        for i in range(last_index + 1):
            if i > global_limit:
                continue
            current_limit = i + a[i]
            if current_limit > global_limit:
                global_limit = current_limit
            if global_limit >= last_index:
                return True
        return False
