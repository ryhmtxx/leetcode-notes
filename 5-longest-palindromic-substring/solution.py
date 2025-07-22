#5. Longest palindromic substring
# s = "cbbd"
class Solution:
    def longestPalindromeBF(self,s:str) -> str:
        # max_len = 0
        ans = ""
        # tmp = []
        n = len(s)
        for left in range(n):
            # print("left",left)
            # tmp.append(s[left])#c
            for right in range(left,n):
                # print(right)
                # tmp.append(s[right])
                tmp = s[left:right+1]
                if tmp == tmp[::-1] and len(tmp) > len(ans):
                    ans = tmp
        return ans

    def longestPalindromeDP(self,s:str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0,0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i,i+1]

        for diff in range(2,n):
            for i in range(n-diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = [i,j]

        i,j = ans

        return s[i:j+1]









            
