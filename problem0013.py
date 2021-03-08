class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """

    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        target_len = len(target)
        source_len = len(source)
        if source_len < target_len:
            return -1
        if source_len == target_len:
            if source == target:
                return 0
            else:
                return -1
        hash_size = 1000000
        hash_factor = 33
        max_factor = 1
        target_hash_code = 0
        for i in range(target_len):
            target_hash_code = (target_hash_code * hash_factor + ord(target[i])) % hash_size
            max_factor *= hash_factor
        current_hash_code = 0
        for i in range(target_len):
            current_hash_code = (hash_factor * current_hash_code + ord(source[i])) % hash_size
        if current_hash_code == target_hash_code and source[0:target_len] == target:
            return 0
        for start in range(1, len(source) - target_len + 1):
            current_hash_code = (current_hash_code * hash_factor + ord(source[start + target_len - 1]) - ord(
                source[start - 1]) * max_factor) % hash_size
            if current_hash_code == target_hash_code and source[start:start + target_len] == target:
                return start
        return -1
