height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
water = 0
head = 0
tail = len(height) - 1

for cnt in range(len(height)):

    width = abs(head - tail)
    # print(head, tail)

    if height[head] < height[tail]:
        res = width * height[head]
        # print(width, height[head], res)
        head += 1
    else:
        res = width * height[tail]
        # print(width, height[tail], res)
        tail -= 1

    if res > water:
        water = res

print(water)