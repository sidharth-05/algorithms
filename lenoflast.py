class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        print(len(s))
        if s == "" or s == " "*(len(s)):
            return 0
        a = s.split(" ")
        if a[len(a) - 1] == "":
            for i in range(a.count("")):
                a.remove("")
            return len(a[len(a) - 1])
        return len(a[-1])