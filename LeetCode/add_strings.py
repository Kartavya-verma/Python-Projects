class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        res= ""
        p1 = len(num1)-1
        p2 = len(num2)-1
        while p1>=0 or p2>=0:
            # if p1>=0 and p2>=0:
            #     res+=str((int(num1[p1])+int(num2[p2])+carry)%10)
            #     carry = (int(num1[p1])+int(num2[p2])+carry)//10
            #     p1-=1
            #     p2-=1
            if p1>=0:
                x1 = ord(num1[p1]) - ord('0')
                # res+=str((int(num1[p1])+carry)%10)
                # carry = (int(num1[p1])+carry)//10
            else:
                x1 = 0
            if p2>=0:
                x2 = ord(num2[p2]) - ord('0')
                # res+=str((int(num2[p2])+carry)%10)
                # carry = (int(num2[p2])+carry)//10
            else:
                x2 = 0
            sum = x1 + x2 + carry
            value = sum % 10
            res += str(value)
            carry = sum // 10
            p1 -= 1
            p2 -= 1

        if carry:
            res+=str(carry)
        return res[::-1]

num1 = input()
num2 = input()
carry = 0
res = ""
p1 = len(num1) - 1
p2 = len(num2) - 1
while p1 >= 0 or p2 >= 0:
    x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
    x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
    sum = x1 + x2 + carry
    value = sum % 10
    res += value
    carry = sum // 10
    p1 -= 1
    p2 -= 1

if carry:
    res += carry
res[::-1]