class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        n = (len(s)) - 1
        while i < n:
            s[i], s[n] = s[n], s[i]
            i+=1
            n-=1

        return s
            