import re


class FileSystem(object):

    class File(object):

        def __init__(self, name, content):
            self.name = name
            self.content = content

        def get_name(self):
            return self.name

        def add_content(self, content):
            self.content += content

        def get_content(self):
            return self.content

        def is_file(self):
            return True

        def if_directory(self):
            return False

    class Directory(object):

        def __init__(self, name):
            self.name = name
            self.childs = {}

        def get_name(self):
            return self.name

        def add_child(self, child):
            self.childs[child.get_name()] = child

        def get_childs(self):
            return sorted(self.childs.keys())

        def get_child_by_name(self, name):
            return self.childs.get(name)

        def is_file(self):
            return False

        def if_directory(self):
            return True

    def __init__(self):
        self.root = FileSystem.Directory("/")

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        if path == "/":
            return self.root.get_childs()
        else:
            cwd = self.root
            for m in re.finditer(r"/([a-z]+)", path):
                name = m.group(1)
                cwd = cwd.get_child_by_name(name)
            if cwd.is_file():
                return [cwd.get_name()]
            if cwd.if_directory():
                return cwd.get_childs()

    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        cwd = self.root
        for m in re.finditer(r"/([a-z]+)", path):
            name = m.group(1)
            next_cwd = cwd.get_child_by_name(name)
            if next_cwd == None:
                child = FileSystem.Directory(name)
                cwd.add_child(child)
                next_cwd = child

            cwd = next_cwd

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        last_cwd = cwd = self.root
        for m in re.finditer(r"/([a-z]+)", filePath):
            name = m.group(1)
            last_cwd = cwd
            cwd = cwd.get_child_by_name(name)
        if cwd == None:
            child = FileSystem.File(name, content)
            last_cwd.add_child(child)
        else:
            cwd.add_content(content)

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        cwd = self.root
        for m in re.finditer(r"/([a-z]+)", filePath):
            name = m.group(1)
            cwd = cwd.get_child_by_name(name)
        return cwd.get_content()

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
