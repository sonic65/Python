from collections import deque

q = deque(["Eric", "John", "Michael"])
print(q)
q.append("Terry")
print(q)
q.popleft() #先进先出
print(q)
q.popright()
print(q)