class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """

    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        circuit_len = len(gas)
        first_position = 0
        while first_position < circuit_len:
            path_len = 0
            sum_of_cost = 0
            sum_of_gas = 0
            while path_len < circuit_len:
                current_pos = (first_position + path_len) % circuit_len
                sum_of_cost += cost[current_pos]
                sum_of_gas += gas[current_pos]
                if sum_of_cost > sum_of_gas:
                    break
                else:
                    path_len += 1
            if path_len == circuit_len:
                return first_position
            first_position += path_len + 1
        return -1
