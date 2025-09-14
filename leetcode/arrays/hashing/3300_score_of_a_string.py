class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for letter in range(len(s)):
            if letter == len(s) - 2:
                # second to last value in string
                score += abs(ord(s[letter]) - ord(s[letter+1]))
                break
            score += abs(ord(s[letter]) - ord(s[letter+1]))

        return score