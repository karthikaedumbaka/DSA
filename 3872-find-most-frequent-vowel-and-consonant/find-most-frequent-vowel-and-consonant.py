from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        #BF
        # vowels=["a","e","i","o","u"]
        # vowels_freq=dict()
        # consonant_freq=dict()
        # for i in s:
        #     if i in vowels:
        #         if i in vowels_freq:
        #             # print(i)
        #             vowels_freq[i]+=1
        #         else:
        #             vowels_freq[i]=1
        #     else:
        #         if i in consonant_freq:
        #             # print(i)
        #             consonant_freq[i]+=1
        #         else:
        #             consonant_freq[i]=1
        # # print(vowels_freq.values())
        # # print(consonant_freq.values())
        # vowels_max=max(vowels_freq.values())  if vowels_freq else 0
        # consonant_max=max(consonant_freq.values())  if consonant_freq else 0

        # return vowels_max + consonant_max
        vowels="aeiou"
        string_freq=Counter(s)
        vowels_max=0
        consonant_max=0
        for i in s:
            if i in vowels:
                if string_freq[i] > vowels_max:
                    vowels_max=string_freq[i]
            else:
                if string_freq[i] > consonant_max:
                    consonant_max=string_freq[i]
        # print(vowels_max)
        # print(consonant_max)
        return  (vowels_max + consonant_max)

        # time O(n)
        # space O(n)

