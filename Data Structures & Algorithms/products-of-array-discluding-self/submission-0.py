class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        P=[1] * len(nums)
        S=[1] * len(nums)
        result=[1] * len(nums)

        for i in range(1, len(nums)):
            P[i] = P[i-1] * nums[i-1]   # changed i+1 -> i-1

        for i in range(1, len(nums)):
            S[-i-1] = S[-i] * nums[-i]  # changed formula

        for i in range(len(nums)):
            result[i] = P[i] * S[i]

        return result