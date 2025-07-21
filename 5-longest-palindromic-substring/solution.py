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
        dp = 






            
