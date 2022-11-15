# User function Template for Python3

class Solution:
    def solve(self, s1, s2, arr, i, N):
        if s1 == s2:
            return True
        
        if s1 > s2:
            i -= 1
            return False

        if s1 < s2 and i < N - 1:
            i += 1    
            if self.solve(s1 + arr[i], s2 - arr[i], arr, i, N):
                return True
            if self.solve(s1, s2, arr, i, N):
                return True
            i -= 1
        return False
            

    def equalPartition(self, N, arr):
        s1 = 0
        s2 = sum(arr)
        i = 0
        return self.solve(s1, s2, arr, i, N)


#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends