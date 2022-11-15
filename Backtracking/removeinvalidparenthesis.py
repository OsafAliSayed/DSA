class Solution:
    def is_valid(self, s):
        stack = []
        for c in s:
            if c == "(":
                stack.append("(")
            elif c == ")":                
                if len(stack) > 0 and (stack[len(stack) - 1] == "("):
                    stack.pop()
                else:
                    stack.append(")")

        return len(stack)

    def solve(self, s, ans, ind, mp):
        if s in mp.keys():
            return
        else:
            mp[s] = 1

        if ind == 0:
            if self.is_valid(s) == 0:
                if s not in ans:
                    ans.append(s)
            return

        for i in range(len(s)):
            if s[i] == '(' or s[i] == ')':
                temp = s[:i] + s[i + 1:]
                self.solve(temp, ans, ind - 1, mp)
                temp = s
        return

    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans = []
        ind = self.is_valid(s)
        mp = {}
        self.solve(s, ans, ind, mp)
        return ans

ob = Solution()
print(ob.removeInvalidParentheses("()((((((()l("))