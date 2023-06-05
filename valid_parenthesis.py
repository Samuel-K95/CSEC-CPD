class Solution:
    def isValid(self, s: str) -> bool:
        left=[]
        right=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                left.append(i)
            else:
                right.append(i)
                left.reverse()
                if i==')':
                    if len(left)>0 and left[0]=='(':
                        left.remove('(')
                        right.remove(i)
                    left.reverse()
                elif len(left)>0 and i==']':
                    if left[0]=='[':
                        left.remove('[')
                        right.remove(i)
                    left.reverse()
                elif len(left)>0 and i=='}':
                    if left[0]=='{':
                        left.remove('{')
                        right.remove(i)
                    left.reverse()

        if len(left)==0 and len(right)==0: 
            return(True)
        else:
            return(False)
