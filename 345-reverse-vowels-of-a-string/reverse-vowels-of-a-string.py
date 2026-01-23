class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a","A","e","E","i","I","o","O","u","U"}
        l = 0
        r = len(s)-1
        string_list = [i for i in s]
        print(string_list)
        while l < r:
            while  l < r and string_list[l] not in vowels:
                l+=1
            while  l < r and  string_list[r] not in vowels:
                r-=1
            string_list[l] ,string_list[r] = string_list[r],string_list[l]
            l+=1
            r-=1
        return "".join(string_list)


        