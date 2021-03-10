class TinyUrl2:
    def __init__(self, tiny_url_len=6):
        self.next_id = 0
        self.data = {}
        self.key = {}
        self.chars = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                      'z', 'x', 'c', 'v', 'b', 'n', 'm', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Q', 'W',
                      'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X',
                      'C', 'V', 'B', 'N', 'M']
        self.base = len(self.chars)
        self.tiny_url_len = tiny_url_len
        self.common_prefix = "http://tiny.url/"

    def createCustom(self, long_url, key: str) -> str:
        current_id = self.sixty_two_to_ten(key)
        if long_url in self.data.values():
            if current_id not in self.data or self.data[current_id] != long_url:
                return "error"
        else:
            if current_id in self.data:
                return "error"
        self.data[current_id] = long_url
        self.key[current_id] = key
        return self.common_prefix + key

    def longToShort(self, url: str) -> str:
        for id, value in self.data.items():
            if value == url:
                return self.common_prefix + self.key[id]
        current_id = self.next_id
        while current_id in self.data:
            current_id += 1
        self.data[current_id] = url
        self.next_id = current_id + 1
        self.key[current_id] = self.ten_to_sixty_two(current_id)
        return self.common_prefix + self.key[current_id]

    def shortToLong(self, url: str) -> str:
        current_id = self.sixty_two_to_ten(url[len(self.common_prefix):])
        if current_id in self.data:
            return self.data[current_id]
        else:
            return "error"

    def sixty_two_to_ten(self, val: str) -> int:
        current_id = 0
        current_factor = 1
        chars_list = list(val)
        chars_list.reverse()
        for c in chars_list:
            digit = self.index_in_chars(c)
            current_id += digit * current_factor
            current_factor *= self.base
        return current_id

    def ten_to_sixty_two(self, val: int) -> str:
        result = []
        while val != 0:
            result.append(self.chars[int(val % self.base)])
            val //= self.base
        for _ in range(len(result), self.tiny_url_len):
            result.append(self.chars[0])
        result.reverse()
        return "".join(result)

    def index_in_chars(self, c: str) -> int:
        for i in range(self.base):
            if self.chars[i] == c:
                return i
        return -1
