# https://leetcode-cn.com/problems/sliding-window-median/solution/hua-dong-chuang-kou-zhong-wei-shu-by-lee-7ai6/

class DualHeap:
    def __init__(self, k: int) -> None:
        # 大根堆，维护较小的一半元素，注意 python 没有大根堆，需要将所有元素取相反数并使用小根堆
        self.small = list()

        # 小根堆，维护较大的一半元素
        self.large = list()

        # 哈希表，记录「延迟删除」的元素，key 为元素，value 为需要删除的次数
        self.delayed = {}

        # small 和 large 当前包含的元素个数，需要扣除被「延迟删除」的元素
        self.smallSize = 0
        self.largeSize = 0

    # 不断地弹出 heap 的堆顶元素，并且更新哈希表
    def prune(self, heap: list) -> None:
        import heapq
        while heap:
            num = heap[0]
            if heap is self.small:
                num = -num
            if num not in self.delayed:
                return
            if self.delayed[num] == 1:
                self.delayed.pop(num)
            else:
                self.delayed[num] -= 1
            heapq.heappop(heap)

    # 调整 small 和 large 中的元素个数，使得二者的元素个数满足要求
    def make_balance(self) -> None:
        import heapq
        if self.smallSize > self.largeSize + 1:
            # small 比 large 元素多 2 个
            heapq.heappush(self.large, -heapq.heappop(self.small))
            self.smallSize -= 1
            self.largeSize += 1
            # small 堆顶元素被移除，需要进行 prune
            self.prune(self.small)
        elif self.smallSize < self.largeSize:
            # large 比 small 元素多 1 个
            heapq.heappush(self.small, -heapq.heappop(self.large))
            self.smallSize += 1
            self.largeSize -= 1
            # large 堆顶元素被移除，需要进行 prune
            self.prune(self.large)

    def insert(self, num: int) -> None:
        import heapq
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.smallSize += 1
        else:
            heapq.heappush(self.large, num)
            self.largeSize += 1
        self.make_balance()

    def erase(self, num: int) -> None:
        if num not in self.delayed:
            self.delayed[num] = 0
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.smallSize -= 1
            self.prune(self.small)
        else:
            self.largeSize -= 1
            self.prune(self.large)
        self.make_balance()

    def get_median(self) -> int:
        return -self.small[0]


class Solution:
    def medianSlidingWindow(self, nums: list, k: int) -> list:
        if not nums or k == 0:
            return []
        dh = DualHeap(k)
        for num in nums[:k]:
            dh.insert(num)
        ans = [dh.get_median()]
        for i in range(k, len(nums)):
            dh.insert(nums[i])
            dh.erase(nums[i - k])
            ans.append(dh.get_median())
        return ans
