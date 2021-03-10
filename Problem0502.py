class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MiniCassandra:

    def __init__(self):
        self.data = {}

    """
    @param: row_key: a string
    @param: column_key: An integer
    @param: value: a string
    @return: nothing
    """

    def insert(self, row_key: str, column_key: int, value: str) -> None:
        if row_key not in self.data:
            self.data[row_key] = []
        old_value_index = -1
        for i in range(len(self.data[row_key])):
            if self.data[row_key][i].key == column_key:
                old_value_index = i
                break
        if old_value_index != -1:
            self.data[row_key][old_value_index].value = value
        else:
            self.data[row_key].append(Column(column_key, value))

    """
    @param: row_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """

    def query(self, row_key: str, column_start: int, column_end: int) -> list:
        result = []
        if row_key in self.data:
            for entry in self.data[row_key]:
                if column_start <= entry.key <= column_end:
                    result.append(entry)
            result.sort(key=lambda e: e.key)
        return result
