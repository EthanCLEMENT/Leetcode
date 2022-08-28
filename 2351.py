class Solution:
    def repeatedCharacter(self, s: str) -> str:
        st=set()
        for i in s:
            if i in st:
                return i
            st.add(i)
