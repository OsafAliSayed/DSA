#User function Template for python3

class Solution:
    """
        m - puzzle 
        x - row 
        y - column
        n - size of puzzle 
        v - visited array
        s - solution string
    """
    # determines whether a given coordinate x, y is safe or not
    def isSafe(self, m, x, y, n, v):
        if (x < n and x >= 0) and (y < n and y >= 0):
            if m[x][y] == 1 and  v[x][y] != 1:
                return True
        return False 
    
    def solve(self, m, x, y, n, v, s, ans):
        # check if start is zero
        if m[0][0] == 0:
            return ans

        # append string in ans if end of puzzle is reached 
        if x == n - 1 and y == n - 1:
            ans.append(s)
            return

        # DLRU moves
        i = [x + 1, x, x, x - 1]
        j = [y, y - 1, y + 1, y]
        moves = ["D", "L", "R", "U"]
        # setting visited as true 
        v[x][y] = 1
        for a in range(4):
            if self.isSafe(m, i[a], j[a], n, v):
                self.solve(m, i[a], j[a], n, v, s + moves[a], ans)      
            
        # backtracking
        v[x][y] = 0    
        

    def findPath(self, m, n):
        # visited array
        v = [[0 for i in range(n)] for i in range(n)]

        # ans array to keep track of all answers 
        ans = []

        # solving the puzzle 
        self.solve(m, 0, 0, n, v, "", ans)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        print(result)
#         result.sort()
#         if len(result) == 0 :
#             print(-1)
#         else:
#             for x in result:
#                 print(x,end = " ")
#             print()
# # } Driver Code Ends