class NestedInteger(object):
    def isInteger(self):
        return True
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        return 0
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        return []
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer


class NestedIterator(object):

    # 注意，next()和hasNext()的算法可以处理特殊的输入：[[], []]

    def __init__(self, nestedList) -> None:
        import collections
        self.stack = collections.deque(nestedList)

    # @return {int} the next element in the iteration
    def next(self):
        if self.hasNext():
            return self.stack.popleft().getInteger()
        return None

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self) -> bool:
        while self.stack and not self.stack[0].isInteger():
            front = self.stack.popleft().getList()
            while front:
                self.stack.appendleft(front.pop())
        return len(self.stack) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
