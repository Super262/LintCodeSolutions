class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """

    def consistentHashing(self, n: int) -> list:
        if n <= 0:
            return []
        cluster = [[0, 359, 1]]
        for new_machine_label in range(2, n + 1):
            largest_part_len = cluster[0][1] - cluster[0][0] + 1
            largest_part_index = 0
            for current_part_index in range(1, len(cluster)):
                current_part_len = cluster[current_part_index][1] - cluster[current_part_index][0] + 1
                if current_part_len > largest_part_len:
                    largest_part_index = current_part_index
                    largest_part_len = current_part_len
            x = cluster[largest_part_index][0]
            y = cluster[largest_part_index][1]
            mid = (x + y) // 2
            cluster[largest_part_index][1] = mid
            cluster.append([mid + 1, y, new_machine_label])
        return cluster
