class Solution:
    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """

    @classmethod
    def create(cls, n: int, k: int):
        solution = cls()
        solution.used_ids = set()
        solution.machines = {}
        solution.k = k
        solution.n = n
        return solution

    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """

    def addMachine(self, machine_id: int) -> list:
        import random
        parts_ids = []
        while len(parts_ids) < self.k:
            next_id = random.randrange(0, self.n)
            if next_id not in self.used_ids:
                self.used_ids.add(next_id)
                parts_ids.append(next_id)
        parts_ids.sort()
        self.machines[machine_id] = parts_ids
        return parts_ids

    """
    @param: hashcode: An integer
    @return: A machine id
    """

    def getMachineIdByHashCode(self, hashcode: int) -> int:
        machine_id = -1
        current_distance = self.n
        for key in self.machines:
            parts_ids = self.machines[key]
            for part_id in parts_ids:
                d = part_id - hashcode
                if d < 0:
                    d += self.n
                if d < current_distance:
                    current_distance = d
                    machine_id = key
        return machine_id
