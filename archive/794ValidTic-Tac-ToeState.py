# coding=utf-8
class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        import  itertools
        nx=no=0
        for ch in itertools.chain(*board):
            if ch=="X":
                nx+=1
            if ch=="O":
                no+=1
        if nx-no>1 or nx-no<0:
            return  False
        wx=wo=False
        for row in board:
            if tuple(row)==("X","X","X"):
                wx=True
            if tuple(row)==("O","O","O"):
                wo=True
        for col in zip(*board):
            if col==("X","X","X"):
                wx=True
            if col==("O","O","O"):
                wo=True
        if board[0][0]==board[1][1]==board[2][2]=="X":
            wx=True
        if board[0][0]==board[1][1]==board[2][2]=="O":
            wo=True
        if board[0][2]==board[1][1]==board[2][0]=="X":
            wx=True
        if board[0][2]==board[1][1]==board[2][0]=="O":
            wo=True
        #print(wx,wo,nx,no)
        if wx==wo==True:
            return False
        if wx and nx!=no+1:
            return False
        if wo and no!=nx:
            return False
        return True


board=["XOX","O O","XOX"]
print(Solution().validTicTacToe(board))

