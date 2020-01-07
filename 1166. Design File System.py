from collections import defaultdict


class FileSystem:

    def __init__(self):
        self.root = {}

    def create(self, path: str, value: int) -> bool:
        if path == "" or path[0] != "/":
            return False
        path = path.split("/")[1:]
        if "" in path:
            return False
        d = self.root
        for sub_path in path[:-1]:
            if sub_path in d:
                d = d[sub_path][1]
            else:
                return False
        sub_path = path[-1]
        if sub_path in d:
            return False
        else:
            d[sub_path] = (value, {})
            return True

    def get(self, path: str) -> int:
        if path == "" or path[0] != "/":
            return -1
        path = path.split("/")[1:]
        if "" in path:
            return -1
        d = self.root
        value = -1
        for sub_path in path:
            if sub_path in d:
                value, d = d[sub_path]
            else:
                return -1
        return value

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.create(path,value)
# param_2 = obj.get(path)
