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
            for ei in range(1, len(a) - 1):
                self.union(email_father, a[ei], a[ei + 1])
        email_cluster = {}
        for child in email_father:
            f = email_father[child]
            if f not in email_cluster:
                email_cluster[f] = []
            email_cluster[f].append(child)
        result = []
        for em in email_cluster:
            email_cluster[em].sort()
            email_cluster[em].insert(0, email_user[em])
            result.append(email_cluster[em])
        return result

    def union(self, father: dict, node1: str, node2: str) -> None:
        root_a = self.find_and_compress(father, node1)
        root_b = self.find_and_compress(father, node2)
        if root_b != root_a:
            father[root_b] = root_a
            for v in father:
                if father[v] == root_b:
                    father[v] = root_a

    def find_and_compress(self, father: dict, node_key: str) -> str:
        path = []
        while node_key != father[node_key]:
            path.append(node_key)
            node_key = father[node_key]
        for v in path:
            father[v] = node_key
        return node_key
