class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            s = self.countAndSay(n-1)
            prev = s[0]
            count = 0;
            ans = ""
            for c in s:
                if c == prev:
                    count += 1
                else:
                    ans += str(count)
                    ans += prev
                    prev = c
                    count = 1
            ans += str(count)
            ans += prev
            return ans