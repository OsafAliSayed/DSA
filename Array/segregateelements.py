# https://practice.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1
# User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        positive = list(filter(lambda x: x >= 0, arr))
        negative = list(filter(lambda x: x <= 0, arr))
        count = 0
        for i in positive:
            arr[count] = i
            count += 1 
        
        for i in negative:
            arr[count] = i
            count += 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends