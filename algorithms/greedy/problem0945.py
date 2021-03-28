class Solution:

    # https://leetcode-cn.com/problems/task-scheduler/solution/tong-zi-by-popopop/

    def leastInterval(self, tasks: list, n: int) -> int:
        if n == 0:
            return len(tasks)
        task_frequency = [0] * 26
        for t in tasks:
            task_frequency[ord(t) - ord("A")] += 1
        task_frequency.sort(reverse=True)
        last_part_len = 0
        for i in range(len(task_frequency)):
            if task_frequency[i] == task_frequency[0]:
                last_part_len += 1
        return max(len(tasks), (task_frequency[0] - 1) * (n + 1) + last_part_len)
