class Solution:
    def longestPrefix(self, s: str) -> str:

        m = len(s)

        lps = [0] * m

        len_ = 0
        i = 1

        while i < m:

            if s[i] == s[len_]:
                len_ += 1
                lps[i] = len_
                i += 1

            else:
                if len_ != 0:
                    len_ = lps[len_ - 1]
                else:
                    lps[i] = 0
                    i += 1

        return s[:lps[-1]]