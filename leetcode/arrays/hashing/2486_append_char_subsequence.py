class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # appened to the end of s so that t becomes a subsequence of s
        # a subsequence is a string that can be derived by deleting characters but not messing w/ ordeer
        # we want t to be subsequence of s
        # we look at the characters at both t and s
        # case 1:
        # t and s dont have any equivalent letters
        set_of_s_chars = set(s)
        set_of_t_chars = set(t)

        if set_of_s_chars.isdisjoint(set_of_t_chars):
            return len(t)

        # case 2:
        # t is already a subsequence of s
        # if this is true, then we return 0
        if t in s:
            return 0

        # case 3:
        # t and s have some equivalent letters IN order.
        # loop through both s and t
        # only increment j if characters are equal (to keep in order)
        # return however far you get in the string j
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1

        return len(t) - j
