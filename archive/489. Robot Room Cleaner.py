# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # turn left direction +1
        # turn right direction -1
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        visited = set([])

        def solve(x, y, direction):
            if (x, y) not in visited:
                robot.clean()
                visited.add((x, y))
                for _ in range(4):
                    if robot.move():
                        dx, dy = directions[direction]
                        solve(x + dx, y + dy, direction)
                        robot.turnLeft()
                        robot.turnLeft()
                        robot.move()
                        robot.turnLeft()
                        robot.turnLeft()
                    robot.turnLeft()
                    direction = (direction + 1) % 4

        solve(0, 0, 0)
