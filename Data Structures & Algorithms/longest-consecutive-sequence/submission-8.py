class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=1
        curlong=1
        n=len(nums)
        i=0
        j=1
        nums=sorted(nums)
        if n<=1:
            return n
        while j<n:

            if (nums[j]-nums[i]==1):                
                curlong=curlong+1
                if curlong>longest:
                    longest=curlong
            elif nums[j]==nums[i]:
                 i=i+1
                 j=j+1
                 continue
                 
             
                           
            else:
                curlong=1
            i=i+1
            j=j+1
        
        return longest
               
        