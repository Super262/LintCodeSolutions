class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    def isMatch(self, s: str, p: str) -> bool:
        if s is None or p is None:
            return False
        memo = [[False] * len(s) for _ in range(len(p))]
        visited = [[False] * len(s) for _ in range(len(p))]
        return self.is_match_helper(s, 0, p, 0, memo, visited)

    def is_match_helper(self, s: str, s_start: int, p: str, p_start: int, memo: list, visited: list) -> bool:
        if p_start == len(p):
            return s_start == len(s)
        if s_start == len(s):
            return self.all_star(p, p_start)
        if visited[p_start][s_start]:
            return memo[p_start][s_start]
        if p[p_start] == "*":
            current_result = self.is_match_helper(s, s_start + 1, p, p_start, memo, visited) \
                             or self.is_match_helper(s, s_start, p, p_start + 1, memo, visited)
        else:
            current_result = self.is_matched(s[s_start], p[p_start]) \
                             and self.is_match_helper(s, s_start + 1, p, p_start + 1, memo, visited)
        visited[p_start][s_start] = True
        memo[p_start][s_start] = current_result
        return current_result

    def all_star(self, p: str, p_start: int) -> bool:
        for i in range(p_start, len(p)):
            if p[i] != "*":
                return False
        return True

    def is_matched(self, s_ch: str, p_ch: str) -> bool:
        return s_ch == p_ch or p_ch == "?"
