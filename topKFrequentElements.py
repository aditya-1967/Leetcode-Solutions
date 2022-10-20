# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        sort = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        
        return [x[0] for x in sort[:k]]
