class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        x = freq.most_common(k)
        l = []
        for a in x:
            l.append(a[0])
        return l
