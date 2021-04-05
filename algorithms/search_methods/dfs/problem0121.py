class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    def findLadders(self, start: str, end: str, word_dict: set) -> list:
        results = []
        word_dict.add(start)
        word_dict.add(end)
        indices = self.build_indices(word_dict)
        distance = self.bfs_get_distance_from_end(end, indices, word_dict)
        self.dfs_get_path_from_start(start, end, indices, distance, [start], results)
        return results

    def dfs_get_path_from_start(self, current: str, target: str, indices: dict, distance: dict, path: list,
                                results: list) -> None:
        if current == target:
            results.append(list(path))
            return
        for n in self.get_neighbors(current, indices):
            if distance[n] != distance[current] - 1:
                continue
            path.append(n)
            self.dfs_get_path_from_start(n, target, indices, distance, path, results)
            path.pop()

    def bfs_get_distance_from_end(self, end: str, indices: dict, word_dict: set) -> dict:
        distance = {end: 0}
        queue = [end]
        while queue:
            end = queue[0]
            queue = queue[1:len(queue)]
            for n in self.get_neighbors(end, indices):
                if n in distance:
                    continue
                distance[n] = distance[end] + 1
                queue.append(n)
        import sys
        for w in word_dict:
            if w in distance:
                continue
            distance[w] = sys.maxsize
        return distance

    def build_indices(self, word_dict: set) -> dict:
        indices = {}
        for word in word_dict:
            for i in range(len(word)):
                key = word[0:i] + "%" + word[i + 1:len(word)]
                if key not in indices:
                    indices[key] = set()
                indices[key].add(word)
        return indices

    def get_neighbors(self, word: str, indices: dict) -> list:
        neighbors = []
        for i in range(len(word)):
            key = word[0:i] + "%" + word[i + 1:len(word)]
            neighbors.extend(indices[key])
        return neighbors
