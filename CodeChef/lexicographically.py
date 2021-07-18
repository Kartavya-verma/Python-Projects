# from itertools import permutations
# li=[''.join(p) for p in permutations(input())]
# print(li)
# s=input()
# if(s==s[::-1]):
#     print("Palin")
# else:
#     print("not")

def lexSmallest(a, n):
    a.sort(reverse=True)
    answer = ""
    for i in range(n):
        answer += a[i]
    return answer
if __name__ == "__main__":
    s=input()
    a = [i for i in s]
    print(a)
    n = len(a)
    print(lexSmallest(a, n))