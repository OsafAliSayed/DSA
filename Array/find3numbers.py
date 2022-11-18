#User function Template for python3
class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self , a, n, X):
        a.sort()
        for i in range(n - 1):
            s = X - a[i]
            j = i + 1
            k = n - 1
            while j < k:
                if (a[j] + a[k]) == s:
                    return True
                elif (a[j] + a[k]) < s:
                    j += 1
                else:
                    k -= 1
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,X=map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)
# } Driver Code Ends