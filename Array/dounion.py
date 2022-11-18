# https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1
#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        s = set()
        for i in a:
            s.add(i)
        for i in b:
            s.add(i)
        
        return len(list(s))
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends