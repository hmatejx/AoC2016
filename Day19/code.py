from collections import deque

input = 3005290

# Part 1
elves = deque()
for i in range(1, input + 1):
    elves.append(i)
while len(elves) > 1:
    e = elves.popleft()
    elves.popleft()
    elves.append(e)
print("Part 1: {}".format(elves[0]))

# Part 2
left = deque()
right = deque()
for i in range(1, input + 1):
    if i < (input // 2) + 1:
        left.append(i)
    else:
        right.appendleft(i)
while left and right:
    if len(left) > len(right):
        left.pop()
    else:
        right.pop()
    right.appendleft(left.popleft())
    left.append(right.pop())
print("Part 2: {}".format(left[0] or right[0]))
