class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        self.vec2d = vec2d
        self.current_row = 0
        self.current_col = -1

    # @return {int} a next element
    def next(self) -> int:
        return self.vec2d[self.current_row][self.current_col]

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self) -> bool:
        self.current_col += 1
        while self.current_row < len(self.vec2d) and self.current_col >= len(self.vec2d[self.current_row]):
            self.current_col = 0
            self.current_row += 1
        return self.current_row < len(self.vec2d)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
