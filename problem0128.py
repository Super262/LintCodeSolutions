class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """

    def hashCode(self, key, HASH_SIZE):
        # This solution won't exceed the time limit.
        result = 0
        key_len = len(key)
        for i in range(key_len):
            result *= 33
            result += ord(key[i])
            result %= HASH_SIZE
        return result
