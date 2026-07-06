class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        st=[]
        for ch in s:
            if ch in '({[':
                st.append(ch)
            else:
                if dic[ch]!=st.pop():
                    return False
        return True