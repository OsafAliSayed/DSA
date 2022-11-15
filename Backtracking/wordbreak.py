#User function Template for python3

class Solution:
    def is_valid_partition(self, n, dict, s):
        if s in dict: 
            return True 
        return False
    
    def solve(self, n, dict, s, ans, words):
        if s == "":
            x = " ".join(words)
            ans.append(x)
            return

        for i in range(1, len(s) + 1, 1):
            if self.is_valid_partition(n , dict, s[:i]):
                words.append(s[:i])
                if self.solve(n, dict, s[i:len(s)], ans, words):
                    return True
                words.pop()
        return False


        
    def wordBreak(self, n, dict, s):
        ans = []
        words = []
        self.solve(n, dict, s, ans, words)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        dicti = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.wordBreak(n, dicti, s)
        print(ans)
        # if(len(ans) == 0):
        #     print("Empty")
        # else:
        #     ans.sort()
        #     for it in (ans):
        #         print("("+it,end = ")")
        #     print()
# } Driver Code Ends