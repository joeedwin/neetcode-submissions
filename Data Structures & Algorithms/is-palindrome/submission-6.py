class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        
        while(i<j):
            while not s[i].isalnum()  :
                i=i+1
                if i==len(s):
                    break
                
            while not s[j].isalnum():
                j=j-1
                if j==0:
                    break
   
            if j==0 or i==len(s):
                continue
            if s[i].lower()!=s[j].lower():
                return False
            else :
                i=i+1
                j=j-1
            
        return True

        