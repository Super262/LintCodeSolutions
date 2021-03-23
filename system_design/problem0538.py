class Memcache:
    def __init__(self):
        self.data = {}
        self.life = {}
        self.birth = {}
        self.invalid_value = 2147483647

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """

    def get(self, curtTime: int, key: int) -> int:
        if key not in self.data or self.birth[key] > curtTime or (
                self.life[key] > 0 and curtTime >= self.birth[key] + self.life[key]):
            return self.invalid_value
        else:
            return self.data[key]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """

    def set(self, curtTime: int, key: int, value: int, ttl: int) -> None:
        self.data[key] = value
        self.life[key] = ttl
        self.birth[key] = curtTime

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """

    def delete(self, curtTime: int, key: int) -> None:
        self.data.pop(key)
        self.birth.pop(key)
        self.life.pop(key)

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """

    def incr(self, curtTime: int, key: int, delta: int) -> int:
        if key not in self.data or self.birth[key] > curtTime or (
                self.life[key] > 0 and curtTime >= self.birth[key] + self.life[key]):
            return self.invalid_value
        else:
            self.data[key] += delta
            return self.data[key]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """

    def decr(self, curtTime: int, key: int, delta: int) -> int:
        if key not in self.data or self.birth[key] > curtTime or (
                self.life[key] > 0 and curtTime >= self.birth[key] + self.life[key]):
            return self.invalid_value
        else:
            self.data[key] -= delta
            return self.data[key]
