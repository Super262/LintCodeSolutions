class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """

    def findCircleNum(self, m: list) -> int:

        # 输入数据无效时，返回0
        if not m or not m[0]:
            return 0

        # 为避免污染源数据，我们使用bool类型数组visited指示节点的状态。初始时，所有节点均未被访问。
        # visited无需为二维数组，因为我们只关注节点，不关注边
        visited = [False] * len(m)

        # 计数器
        count = 0

        for i in range(len(m)):
            # 若节点存在且未被访问，开始BFS
            if m[i][i] == 1 and not visited[i]:
                self.bfs(m, visited, i)
                # BFS结束后，计数器加1
                count += 1
        return count

    def bfs(self, m: list, visited: list, start: int) -> None:
        import collections
        # 起点入队，切记将visited[start]设置为True
        q = collections.deque([start])
        visited[start] = True
        while q:
            node = q.popleft()
            for i in range(len(m[node])):
                # 可以入队的邻居：有效、可达并且未被访问过的节点
                if m[i][i] == 0 or m[node][i] == 0 or visited[i]:
                    continue
                q.append(i)
                # 邻居入队后，改变邻居节点的状态
                visited[i] = True
