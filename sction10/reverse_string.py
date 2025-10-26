# plan: using two pointer, which is wordStartIndex, and runner
from typing import List


class Solution:
  def reverseWords(self, s: str) -> str:
    
    def swap(s_list:List[str], start:int, end:int):
      while start < end:
        s_list[start], s_list[end] = s_list[end], s_list[start]
        start += 1
        end -= 1
      return s_list
      
    # step1: linear scan left => right
    s_list = list(s)
    wordStartIndex = 0
    runner = 0
    
    while runner < len(s):
      # step: if runner encounter ' ', then swap the word between s[wordStartIndex, runner
      if s[runner] == ' ':
        swap(s_list, wordStartIndex, runner-1)
        wordStartIndex = runner + 1
        
      if runner == len(s) -1:
        swap(s_list, wordStartIndex, runner)
      
      runner = runner + 1
        
    return "".join(s_list)
       