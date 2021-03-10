class TinyUrl:
    def __init__(self, tiny_url_len=6):
        self.next_id = 0
        self.data = {}
        self.chars = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                      'z', 'x', 'c', 'v', 'b', 'n', 'm', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Q', 'W',
                      'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X',
                      'C', 'V', 'B', 'N', 'M']
        self.base = len(self.chars)
        self.tiny_url_len = tiny_url_len
        self.common_prefix = "http://tiny.url/"

    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """

    def longToShort(self, url: str) -> str:
        current_id = self.next_id
        result = []
        while current_id != 0:
            result.append(self.chars[int(current_id % self.base)])
            current_id //= self.base
        for _ in range(len(result), self.tiny_url_len):
            result.append(self.chars[0])
        result.reverse()
        self.data[self.next_id] = url
        self.next_id += 1
        return self.common_prefix + ("".join(result))

    """
    @param: url: a short url starts with http://tiny.url/
    @return: a long url
    """

    def shortToLong(self, url: str) -> str:
        current_id = 0
        current_factor = 1
        chars_list = list(url[len(self.common_prefix):])
        chars_list.reverse()
        for c in chars_list:
            digit = self.sixty_two_to_ten(c)
            current_id += digit * current_factor
            current_factor *= self.base
        return self.data[current_id]

    def sixty_two_to_ten(self, c: str) -> int:
        for i in range(self.base):
            if self.chars[i] == c:
                return i