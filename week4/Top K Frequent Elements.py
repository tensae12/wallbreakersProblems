class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = collections.Counter(nums)
        most_com_elements = counted.most_common(k)
        return [pair[0] for pair in most_com_elements]
        