class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False
        target = Counter(s1)
        window = Counter(s2[:n])
        if target == window:
            return True

        for i in range(n, m):
            window[s2[i]] += 1
            left = s2[i-n]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            if window == target:
                return True

        return False