class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for i in strs:
                sorted_word = "".join(sorted(i))
                if sorted_word in dictionary:
                    dictionary[sorted_word].append(i)
                else:
                    dictionary[sorted_word] = [i]
        return dictionary.values()
                
            
