import pdb
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import string
        # table = string.maketrans("", "")
        # paragraph = paragraph.translate(table, string.punctuation)
        paragraph = paragraph.replace("!", "").replace("?", "").replace("'", "").replace(",","").replace(";","").replace(".","")
        paragraph = [i.lower() for i in paragraph.split()]
        
        s = 0 
        word_dict = {}
        ans = "", 0
        while s < len(paragraph):
            curr_word = paragraph[s]
            if curr_word not in banned:
                if curr_word not in word_dict:
                    word_dict[curr_word] = word_dict.get(curr_word,0) +1
                else:
                    word_dict[curr_word] +=1
                if word_dict[curr_word] > ans[1]:
                    ans = curr_word, word_dict[curr_word]
            # if s == len(paragraph) -1:
                # pdb.set_trace()          
            s+=1
        
        return ans[0]

s = Solution()
ans = s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
print(ans)