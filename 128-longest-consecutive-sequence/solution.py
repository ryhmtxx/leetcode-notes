class Solution:
    def longestConsecutive(self,nums:List[int]) -> int:
        # put all nums in a set: unique, search complexity n(1)
        num = set(nums)
        longest = 0

        for item in num:
            # check if item is the start of a streak
            if item - 1 not in num:
                current = item
                length = 1

                while current + 1 in num:
                    current += 1
                    length += 1
                
                longest = max(length,longest)
        return longest