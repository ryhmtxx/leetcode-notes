#1.Two Sum
class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        # make a dict for recording all traversed elements
        records = dict()
        for idx, value in enumerate(nums):
            if target - value in records:
                return [idx,records[target-value]]
            # record the value and its index in the dict
            records[value] = idx
        return []
