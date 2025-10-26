import math
from typing import List


class Solution():
  def majority_element(self, nums: List[int]) -> int:
    # step1: add each num add key->num, value->count in map
    map = {}
    for num in nums:
      if num in map:
        map[num] += 1 # add count
      else:
        map[num] = 1 # init count in 1
        
    # step2: return the key of count which is > n/2 in map
    majority_count = math.floor(len(nums) / 2.0)
    majority_element = nums[0] # init as someone
    for key, value in map:
      if value > majority_count:
        majority_element = key
    return majority_element;