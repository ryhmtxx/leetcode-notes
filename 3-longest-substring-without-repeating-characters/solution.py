#3. Longest substring without repeating characters
class Solution:
    def lengthOfLongestSubstring(self,s:str) -> int:
        max_length = 0
        # maintain a set to check if it's a non-repeating substring and the length
        records = set()
        n = len(s)
        left = 0

        for right in range(n):
            # means the element s[right] is not in the current substing yet, put it in and update the length
            if s[right] not in records:
                records.add(s[right])
                max_length = max(right - left + 1,max_length)
            
            else:
                #if the new s[right] in the current substring, remove all the elements in the records now
                while s[right] in records:
                    records.remove(s[left])
                    left += 1
                # then add the latest element
                records.add(s[right])
        return max_length
                