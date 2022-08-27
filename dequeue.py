from collections import deque
# [6,5,4,3,1,9,8,7]
# [7,8,9,1,3,4,5,6]
q = deque([4, 5, 6])
q.append(7)
q.appendleft(3)
q.extend([8, 9, 10])
q.extendleft([1, 2])
q.insert(5, -1)
q.pop()
q.popleft()
q.remove(-1)
q.rotate(3)
q.reverse()
print(q)

