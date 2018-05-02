class Solution:
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        from collections import deque
        q = deque([(0, 1, 0)])
        visited = {(0, 1)}
        while q:
            pos, speed, count = q.popleft()
            pos1, speed1 = pos + speed, speed * 2
            if pos1 == target:
                return count + 1
            if (abs(pos1) < target * 2) and (pos1, speed1) not in visited:
                visited.add((pos1, speed1))
                q.append((pos1, speed1, count + 1))
            pos2, speed2 = pos, -1 if speed > 0 else 1
            if (pos2, speed2) not in visited:
                visited.add((pos2, speed2))
                q.append((pos2, speed2, count + 1))
            # print(q)
        return -1
