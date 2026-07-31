class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for ch in tokens:
            if ch in '+-*/':
                a=st.pop()
                if ch=='+':
                    st.append(st.pop()+a)
                elif ch=='-':
                    st.append(st.pop()-a)
                elif ch=='*':
                    st.append(st.pop()*a)
                elif ch=='/':
                    st.append(int(st.pop()/a))
            else:
                st.append(int(ch))
        return st[0]
                
                