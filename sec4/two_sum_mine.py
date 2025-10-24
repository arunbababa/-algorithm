from typing import List


class Solution:
  # measn that you have to find to pair from nums that when to pair are added, becomes taget
  def twoSum(self, nums:List[int], target: int):
    result = []
    map = {} # containes {value: index} ex. {may_be_one_of_result(2): index(1)}
    
    # step 1: linear scan array left => right, and build map
    for i in range(0, len(nums)):
      
      # step 2: check if target - nums[i] in hashmap, if so return indices
      checked = target - nums[i]
      if checked in map: # check key
        # add checked numbers`s index and the already exists in hashmap as value
        result.append(i)
        result.append(map[checked])
        break
      else:
        # step 3: if not exist, then append the maybe_oneof_indcies as key and index as value
        map[nums[i]] = i
    return result