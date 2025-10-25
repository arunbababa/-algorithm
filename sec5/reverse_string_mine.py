from typing import List


class Solution:
  def reverse_string(self, l_list: List[str]):
    # step1: scan with two pointer from_start=> and <=from_end
    start = 0
    end = len(l_list) - 1
    while start < end: # when becomes same value, it means the reverse has been done
      l_list[start], l_list[end] = l_list[end], l_list[start]
      # update start ++, and end --
      start += 1
      end -= 1
      # using the original list, the reverse completed
    return None