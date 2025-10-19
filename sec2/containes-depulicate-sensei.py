class Solution:
    # return true if nums[] contains duplicate
    # pre: nums[1,2,3,1]
    # post: true
    def containsDuplicate(self, nums: List[int]) -> bool:
        # corner case: nums is empty or size 1, return false
        if len(nums) <= 1:
            return False;
        
        # step1: single linear scan left -> right, build hashMap as we go
        map = {}
        
        for num in nums:
            # step 2: if map.containsKey(nums[i]) == true, then dup found so return true
            if num in map:
                return True;
            
            map[num] = True
        
        return False;