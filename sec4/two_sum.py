class Solution:
    # return indeces of two items summing up to target
    # pre: nums[2,7,11,15],target=9
    # post: [0,1]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = []
        map = {}
        
        # step1: linear scan array left -> right, and build map       
        for i in range(0, len(nums)):
            # step 2: check if (target - nums[i]) exists in hashmap, if so return two indices
            complement = target - nums[i]
            if complement in map:
                # return indeces
                results.append(map[complement])
                results.append(i)
                break;
            else:
                # step 3: else, add (nums[i], i) to hashmap
                map[nums[i]] = i
        return results;