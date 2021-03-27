class Solution:

    def accountsMerge(self, accounts: list) -> list:
        if not accounts:
            return []
        email_father = {}
        email_user = {}
        for a in accounts:
            for ei in range(1, len(a)):
                email_user[a[ei]] = a[0]
                email_father[a[ei]] = a[ei]
        for a in accounts:
            for ei in range(2, len(a)):
                self.union(email_father, a[1], a[ei])
        result = []
        email_cluster = {}
        for a in accounts:
            for ei in range(1, len(a)):
                root = self.find_and_compress(email_father, a[ei])
                if root not in email_cluster:
                    email_cluster[root] = set()
                email_cluster[root].add(a[ei])
        for cl_e in email_cluster:
            temp = []
            temp.extend(email_cluster[cl_e])
            temp.sort()
            temp.insert(0, email_user[cl_e])
            result.append(temp)
        return result

    def union(self, father: dict, node1: str, node2: str) -> None:
        # 合并两个集合时，不需要立刻进行路经压缩。只有在查找时，才执行路经压缩。
        root_a = self.find_and_compress(father, node1)
        root_b = self.find_and_compress(father, node2)
        if root_b != root_a:
            father[root_b] = root_a

    def find_and_compress(self, father: dict, node_key: str) -> str:
        path = []
        while node_key != father[node_key]:
            path.append(node_key)
            node_key = father[node_key]
        for v in path:
            father[v] = node_key
        return node_key
