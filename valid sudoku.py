class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowcheck = [0]*10
        colcheck = [0]*10
        
        n = len(board)
        m = len(board[0])

        for i in range(n):
            rowcheck = [0]*10
            for j in range(m):
                if board[i][j] == '.': continue
                if rowcheck[int(board[i][j])] != 0:
                    return False
                rowcheck[int(board[i][j])] = 1
        
        for j in range(m):
            colcheck = [0]*10
            for i in range(n):
                if board[i][j] == '.': continue
                if colcheck[int(board[i][j])] != 0:
                    return False
                colcheck[int(board[i][j])] = 1
        
        check = [0]*10
        # first segment
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.': continue
                if check[int(board[i][j])] != 0:
                    return False
                check[int(board[i][j])] = 1 
        
        check = [0]*10
        # second segment
        for i in range(3):
            for j in range(3,6):
                if board[i][j] == '.': continue
                if check[int(board[i][j])] != 0:
                    return False
                check[int(board[i][j])] = 1 
        
        check = [0]*10
        # Third segment
        for i in range(3):
            for j in range(6,9):
                if board[i][j] == '.': continue
                if check[int(board[i][j])] != 0:
                    return False
                check[int(board[i][j])] = 1 
        
        check = [0]*10
        # fourth segment
        for i in range(3,6):
            for j in range(3):
                if board[i][j] == '.': continue
                if check[int(board[i][j])] != 0:
                    return False
                check[int(board[i][j])] = 1 
        
        check = [0]*10
        # Fifith segment
        for i in range(3,6):
            for j in range(3,6):
                if board[i][j] == '.': continue
                if check[int(board[i][j])] != 0:
                    return False
                check[int(board[i][j])] = 1 
        
        check = [0]*10
        # Sixth segment
        for i in range(3,6):
            for j in range(6,9):
                if board[i][j] == '.': continue
                if check[int(board[i][j])] != 0:
                    return False
                check[int(board[i][j])] = 1 
        
        check = [0]*10
        # Seventh segment
        for i in range(6,9):
            for j in range(3):
                if board[i][j] == '.': continue
                if check[int(board[i][j])] != 0:
                    return False
                check[int(board[i][j])] = 1 

        check = [0]*10
        # Eight segment
        for i in range(6,9):
            for j in range(3,6):
                if board[i][j] == '.': continue
                if check[int(board[i][j])] != 0:
                    return False
                check[int(board[i][j])] = 1 
        
        check = [0]*10
        # Nine segment
        for i in range(6,9):
            for j in range(6,9):
                if board[i][j] == '.': continue
                if check[int(board[i][j])] != 0:
                    return False
                check[int(board[i][j])] = 1 

        # print(rowcheck)
        # print(colcheck)
        return True