class TwoSum:

    def __init__(self):
        self.count = {}

    def add(self, number: int) -> None:
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    def find(self, value: int) -> bool:
        for num1 in self.count:
            num2 = value - num1
            if num2 == num1 and self.count[num1] > 1:
                return True
            if num2 != num1 and num2 in self.count:
                return True
        return False
