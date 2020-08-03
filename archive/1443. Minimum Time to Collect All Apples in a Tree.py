class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        children = {}
        for i, j in edges:
            children.setdefault(i, [])
            children[i].append(j)

        has_apple = {}

        def check_has_apples(root):
            print(root)
            if root == None:
                return False
            if root in has_apple:
                return has_apple[root]
            temp = hasApple[root]
            for child in children.get(root, []):
                temp = check_has_apples(child) or temp
            has_apple[root] = temp
            return has_apple[root]

        check_has_apples(0)

        def cost(root):
            if root == None:
                return 0
            temp = 0
            for child in children.get(root, []):
                if has_apple[child]:
                    temp += cost(child) + 2
            return temp

        return cost(0)