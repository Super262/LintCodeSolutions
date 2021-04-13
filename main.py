def subarraySumClosest(nums: list) -> list:
    prefix_sum = [[0, i] for i in range(len(nums) + 1)]
    for i in range(1, len(prefix_sum)):
        prefix_sum[i][0] = nums[i - 1] + prefix_sum[i - 1][0]
    prefix_sum.sort(key=lambda item: item[0])
    result = [prefix_sum[0][1], prefix_sum[1][1] - 1]
    mis_distance = abs(prefix_sum[0][0] - prefix_sum[1][0])
    for i in range(1, len(prefix_sum)):
        if abs(prefix_sum[i][0] - prefix_sum[i - 1][0]) < mis_distance:
            mis_distance = abs(prefix_sum[i][0] - prefix_sum[i - 1][0])
            result[0] = prefix_sum[i - 1][1]
            result[1] = prefix_sum[i][1]
    result.sort()
    return result


if __name__ == '__main__':
    nums = [6, -4, -8, 3, 1, 7]
    print(subarraySumClosest(nums))
