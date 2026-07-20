class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc=Counter(ransomNote)
        mc=Counter(magazine)

        for ch in rc:
            if rc[ch]!=mc[ch]:
                return False
        return True