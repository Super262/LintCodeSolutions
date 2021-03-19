class Solution:

    def maxNumber(self, nums1: list, nums2: list, k: int) -> list:
        seq1_len = len(nums1)
        seq2_len = len(nums2)
        if k - seq2_len > 0:
            part1_len = k - seq2_len
        else:
            part1_len = 0
        result = [0] * k
        while part1_len <= seq1_len and part1_len <= k:
            part2_len = k - part1_len
            temp = merge_seq_to_max(max_subseq(nums1, part1_len), max_subseq(nums2, part2_len))
            if compare_seq_from_head(temp, 0, result, 0) > 0:
                result = temp[:]
            part1_len += 1
        return result


def max_subseq(seq: list, k: int) -> list:
    stack = [0] * k
    stack_top = -1
    seq_len = len(seq)
    remains_count = seq_len - k
    for i in range(seq_len):
        while stack_top >= 0 and remains_count > 0 and seq[i] > stack[stack_top]:
            stack_top -= 1
            remains_count -= 1
        if stack_top < k - 1:
            stack_top += 1
            stack[stack_top] = seq[i]
        else:
            remains_count -= 1
    return stack


def merge_seq_to_max(seq1: list, seq2: list) -> list:
    seq1_len = len(seq1)
    seq2_len = len(seq2)
    result = [0] * (seq1_len + seq2_len)
    p_r = 0
    p_s1 = 0
    p_s2 = 0
    while p_s1 < seq1_len and p_s2 < seq2_len:
        if compare_seq_from_head(seq1, p_s1, seq2, p_s2) > 0:
            result[p_r] = seq1[p_s1]
            p_s1 += 1
        else:
            result[p_r] = seq2[p_s2]
            p_s2 += 1
        p_r += 1
    while p_s1 < seq1_len:
        result[p_r] = seq1[p_s1]
        p_s1 += 1
        p_r += 1
    while p_s2 < seq2_len:
        result[p_r] = seq2[p_s2]
        p_s2 += 1
        p_r += 1
    return result


def compare_seq_from_head(seq1: list, start1: int, seq2: list, start2: int) -> int:
    seq1_len = len(seq1) - start1
    seq2_len = len(seq2) - start2
    if seq2_len <= seq1_len:
        common_len = seq2_len
    else:
        common_len = seq1_len
    for i in range(common_len):
        if seq1[start1 + i] != seq2[start2 + i]:
            return seq1[start1 + i] - seq2[start2 + i]
    return seq1_len - seq2_len
