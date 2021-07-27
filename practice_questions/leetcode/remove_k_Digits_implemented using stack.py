# https://leetcode.com/problems/remove-k-digits/submissions/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == 1:
            return "0"
        num1 = [int(_) for _ in num]
        stack = []
        stack.append(num[0])
        for i in range(1, len(num1)):
            flag = False
            while len(stack)>0 and k>0:     
                if int(stack[-1]) > num1[i]:
                    stack.pop()
                    k-=1
                else:
                    flag = True
                    break
            if len(stack)==0 or flag:
                stack.append(num[i])
            elif k==0:
                stack.append(num[i])
            # print(stack)
              
        while k>0 and len(stack)>0:
            stack.pop()
            k-=1
            # print("A ", stack)

        return str(int("".join(stack))) if len(stack)!=0 else "0"       
                
