# 744. Find Smallest Letter Greater Than Target
# Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.
# Note that the letters wrap around.
# For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = []
        for i in letters:
            if i > target:
                ans.append(i)
        if len(ans) > 0:
            return ans[0]
        return letters[0]
