class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        half_leng = len(nums) // 2

        heapq.heapify(nums)
        nums.sort()

        pair_left_lst = []
        pair_right_lst = []
        for _ in range(half_leng):
            pair_left_lst.append(heapq.heappop(nums))
            pair_right_lst.append(heapq.heappop(nums))

        answer = sum(pair_left_lst)
        return answer
