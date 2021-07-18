s = "Let's take LeetCode contest"

print(i for i in s.split())
print(" ".join([i[::-1] for i in s.split()]))
