class Solution:
    def sortSentence(self, s: str) -> str:
        store=[i for i in s.split(" ")]
        answer=[i for i in s.split(" ")]
        key=[]
        for i in store:
            key.append(i[-1])
        for i in range(len(store)):
            print
            if store[i][-1]==key[i]:
                answer[int(key[i])-1]= store[i][:-1]
        ans=""
        for i in range(0,len(answer)):
            ans+=answer[i]
            if i!=len(answer)-1:
                ans+=" "
        return ans