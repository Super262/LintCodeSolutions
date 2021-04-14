class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList: list) -> list:
        import collections
        stack = collections.deque([nestedList])
        result = []
        while stack:
            front = stack.popleft()
            if isinstance(front, list):
                while front:
                    stack.appendleft(front.pop())
            else:
                result.append(front)
        return result
