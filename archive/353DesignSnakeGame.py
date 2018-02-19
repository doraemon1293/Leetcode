# coding=utf-8
'''
Created on 2017Âπ?8Êú?22Êó?

@author: Administrator
'''
from collections import deque


def designProbTest(functions, parameters):
    for i in xrange(len(functions)):
        f, para = functions[i], parameters[i]
        if f[0].isupper():
            cls = eval(f + "(*para)")
        else:
            print eval("cls." + f + "(*para)")


class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.food = food
        self.food_ind = 0
        if self.food_ind >= len(self.food):
            self.food_ind = None
        self.width = width
        self.height = height
        self.x = self.y = 0
        self.score = 0
        self.snakes = deque([[0, 0]])
        # print self.food, self.width, self.height

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        x, y = self.snakes[-1]
        if direction == "U":
            x -= 1
        elif direction == "L":
            y -= 1
        elif direction == "R":
            y += 1
        elif direction == "D":
            x += 1

        if self.food_ind != None and x == self.food[self.food_ind][0] and y == self.food[self.food_ind][1]:
            self.food_ind += 1
            if self.food_ind >= len(self.food):
                self.food_ind = None
            self.score += 1
        else:
            self.snakes.popleft()
        if x < 0 or x >= self.height or y < 0 or y >= self.width or [x, y] in self.snakes:  # ÊòØÂê¶Âá∫Ê°Ü
            return -1
        self.snakes.append([x, y])
        return self.score


functions = ["SnakeGame", "move", "move", "move", "move", "move", "move"]
parameters = [[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["R"]]
designProbTest(functions, parameters)

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
