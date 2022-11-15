class Solution:
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        x1 = KnightPos[0]
        y1 = KnightPos[1]
        x2 = TargetPos[0]
        y2 = TargetPos[1]

        # visited array
        v = [[0 for i in range(N)] for i in range(N)]

        # we simply use BST traversal here 

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		KnightPos = list(map(int, input().split()))
		TargetPos = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
		print(ans)

# } Driver Code Ends