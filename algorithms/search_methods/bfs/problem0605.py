class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    # 队列中一直只包含1个元素时，拓扑序是唯一的
    def sequenceReconstruction(self, org: list, seqs: list) -> bool:
        # 有效的拓扑排序：结果长度等于节点个数
        if not org and (not seqs or not seqs[0]):
            return True
        if not seqs or not seqs[0]:
            return False
        if not org:
            return False

        # build the graph
        in_degree = {}
        neighbors = {}
        for s in seqs:
            for v in s:
                in_degree[v] = 0
                neighbors[v] = []
        for s in seqs:
            if len(s) < 2:
                continue
            for i in range(1, len(s)):
                if s[i] not in in_degree:
                    in_degree[s[i]] = 0
                if s[i - 1] not in neighbors:
                    neighbors[s[i - 1]] = []
                in_degree[s[i]] += 1
                neighbors[s[i - 1]].append(s[i])

        start_points = []
        for i in in_degree:
            if in_degree[i] == 0:
                start_points.append(i)
        import collections
        q = collections.deque(start_points)
        order = []
        while q:
            if len(q) > 1:
                return False
            node = q.popleft()
            order.append(node)
            for n in neighbors[node]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    q.append(n)
        return len(order) == len(in_degree) and order == org
