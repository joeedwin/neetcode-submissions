class Solution:
    def isValid(self, s: str) -> bool:
        k=[]
        ji={
            "{":"}",
             "[":"]",
             "(":")"
        }
        last=-1
        for i  in s:
            print(ji.get(i),i,last)
            if i in ji.keys():
                k.append(i)
                last=last+1
            elif len(k)==0:
                return False
            elif ji.get(k[last])==i:
                k.pop()
                last=last-1
            else :
                return False
        if len(k)==0:
            return True
        else :
            return False



