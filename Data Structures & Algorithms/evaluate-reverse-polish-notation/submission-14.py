class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op=['+','-','*','/']
        st=[]

        for i in tokens:
            print(i,st)
            if i not in op:
                st.append(i)
            elif i in op:
                
                x=int(st.pop())
                y=int(st.pop())
                print(x,y,i)
                if i=='+':
                    st.append(x+y)
                if i=='-':
                     st.append(y-x)
                if i=='*':
                    st.append(x*y)
                if i=='/':
                    st.append(int(y/x))
        return int(st.pop())   