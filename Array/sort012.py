# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0
#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        count = [0, 0, 0]
        for i in arr:
            if i == 0:
                count[0] += 1
            elif i == 1:
                count[1] += 1
            else:
                count[2] += 1 
        for i in range(count[0]):
            arr[i] = 0
        for i in range(count[0], count[0] + count[1], 1):
            arr[i] = 1
        for i in range(count[0] + count[1], count[0] + count[1] + count[2], 1):
            arr[i] = 2
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends