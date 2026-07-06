class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        if len(s)==1:
            return False
        st=[]
        for ch in s:
            if ch in '({[':
                st.append(ch)
            else:
                if dic[ch]!=st.pop():
                    return False
        if not st:
            return True
        else:
            return False