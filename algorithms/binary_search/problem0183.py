class Solution:

    def woodCut(self, sticks: list, k: int) -> int:
        if not sticks:
            return 0
        min_each_l = 1
        max_each_l = min(max(sticks), sum(sticks) // k)
        if min_each_l > max_each_l:
            return 0
        while min_each_l + 1 < max_each_l:
            mid = min_each_l + (max_each_l - min_each_l) // 2
            if self.get_pieces_count(sticks, mid) < k:
                max_each_l = mid
            else:
                min_each_l = mid
        if self.get_pieces_count(sticks, max_each_l) >= k:
            return max_each_l
        if self.get_pieces_count(sticks, min_each_l) >= k:
            return min_each_l
        return 0

    def get_pieces_count(self, sticks: list, each_l: int) -> int:
        count = 0
        for s in sticks:
            count += (s // each_l)
        return count
