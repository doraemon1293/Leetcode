class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        pawns=set()
        bishops=set()
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y]=="R":
                    x0,y0=x,y
                if board[x][y]=="B":
                    bishops.add((x,y))
                if board[x][y]=="p":
                    pawns.add((x,y))
        ans=0
        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
            x1,y1=x0+dx,y0+dy
            while 0<=x1<len(board) and 0<=y1<len(board[0]) and (x1,y1) not in pawns and (x1,y1) not in bishops:
                x1,y1=x1+dx,y1+dy
            if (x1,y1) in pawns:
                ans+=1
        return ans


