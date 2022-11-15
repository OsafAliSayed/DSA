#User function Template for python3

class Solution:
    def empty_location(self, grid, l):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    l[0] = i
                    l[1] = j
                    return True
        return False

    def isSafe(self, grid, row, col, num):
        for x in range(9):
            # checking row and column 
            if grid[row][x] == num:
                return False

        for x in range(9):
            # checking row 
            if grid[x][col] == num:
                return False

        # checking the box
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == num:
                    return False

        return True

    def solve(self, grid, n):
        l = [0, 0]
        if (not self.empty_location(grid, l)):
            return True
        row = l[0]
        col = l[1]

        for i in range(1, n + 1, 1):
            if (self.isSafe(grid, row, col, i)):

                grid[row][col] = i

                if (self.solve(grid, n)):
                    return True

                grid[row][col] = 0

        return False
    
    #Function to find a solved Sudoku. 
    def SolveSudoku(self, grid):
        x = self.solve(grid, 9)
        return x
    
    #Function to print grids of the Sudoku.    
    def printGrid(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution() 
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
# } Driver Code Ends