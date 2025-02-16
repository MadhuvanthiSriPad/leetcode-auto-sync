class Solution:
    def reverseWords(self, s: str) -> str:

        s=s.split()
        print(s)
        start,end = 0 , len(s)-1

        while(start<end):
            s[start],s[end]=s[end],s[start]
            start+=1
            end-=1
        return " ".join(s)

        