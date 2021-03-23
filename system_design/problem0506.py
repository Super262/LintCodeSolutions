class BaseGFSClient:
    def readChunk(self, filename: str, chunkIndex: int) -> str:
        return ""

    def writeChunk(self, filename: str, chunkIndex: int, content: str) -> None:
        return


class GFSClient(BaseGFSClient):

    def __init__(self, chunk_size: int):
        BaseGFSClient.__init__(self)
        self.chunk_size = chunk_size
        self.chunk_list_map = {}

    def read(self, filename: str):
        if filename not in self.chunk_list_map:
            return None
        parts_of_result = []
        for index in self.chunk_list_map[filename]:
            parts_of_result.append(self.readChunk(filename, index))
        return "".join(parts_of_result)

    def write(self, filename: str, content: str) -> None:
        self.chunk_list_map[filename] = []
        index = 0
        start = 0
        end = self.chunk_size
        while start < len(content):
            self.writeChunk(filename, index, content[start:end])
            self.chunk_list_map[filename].append(index)
            start += self.chunk_size
            end += self.chunk_size
            index += 1
