class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans


# class Solution:
    # def get Concatenation(self, nums: List[int]) -< List[int]:
        # return nums + nums