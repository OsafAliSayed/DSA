#User function Template for python3

class Solution:
    def isSafe(self, arr, x, y, n):
        for i in range(x):
            if arr[i][y] == 1:
                return False
        
        i = x - 1
        j = y - 1
        while i >= 0 and j >= 0:
            if arr[i][j] == 1:
                return False
            i -= 1
            j -= 1
        
        i = x - 1
        j = y + 1
        while i >= 0 and j < n:
            if arr[i][j] == 1:
                return False
            i -= 1
            j += 1
        
        return True 

    def solve(self, board, x, y, n, solArr):
        # if all queens are placed
        if x == n:
            sol = []
            for i in board:
                for j in range(n):
                    if i[j] == 1:
                        sol.append(j + 1)
            solArr.append(sol)
            return

        for i in range(n):
            if self.isSafe(board, x, i, n):
                board[x][i] = 1
                self.solve(board, x + 1, 0, n, solArr)
                board[x][i] = 0

        return  
        

    def nQueen(self, n):
        board = [[0 for i in range(n)] for i in range(n)]
    
        solArr = []

        self.solve(board, 0, 0, n, solArr)
        return solArr



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends