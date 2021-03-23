class TinyUrl2:
    def __init__(self, tiny_url_len=6):
        self.chars = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                      'z', 'x', 'c', 'v', 'b', 'n', 'm', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Q', 'W',
                      'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X',
                      'C', 'V', 'B', 'N', 'M']
        self.next_id = 0
        self.short_to_long = {}
        self.long_to_short = {}
        self.base = len(self.chars)
        self.tiny_url_len = tiny_url_len
        self.common_prefix = "http://tiny.url/"

    def createCustom(self, long_url, key: str) -> str:
        if key in self.short_to_long and self.short_to_long[key] == long_url:
            return self.common_prefix + key
        if key not in self.short_to_long and long_url not in self.long_to_short:
            self.short_to_long[key] = long_url
            self.long_to_short[long_url] = key
            return self.common_prefix + key
        return "error"

    def longToShort(self, url: str) -> str:
        if url in self.long_to_short:
            return self.common_prefix + self.long_to_short[url]
        current_id = self.next_id
        current_key = self.ten_to_sixty_two(current_id)
        while current_key in self.short_to_long:
            current_id += 1
            current_key = self.ten_to_sixty_two(current_id)
        self.next_id = current_id + 1
        self.long_to_short[url] = current_key
        self.short_to_long[current_key] = url
        return self.common_prefix + current_key

    def shortToLong(self, url: str) -> str:
        url = url[len(self.common_prefix):]
        if url in self.short_to_long:
            return self.short_to_long[url]
        return "error"

    def ten_to_sixty_two(self, val: int) -> str:
        result = []
        while val != 0:
            result.append(self.chars[int(val % self.base)])
            val //= self.base
        for _ in range(len(result), self.tiny_url_len):
            result.append(self.chars[0])
        result.reverse()
        return "".join(result)
