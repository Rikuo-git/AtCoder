# fibonacci
def fib(n):
    global a
    a=[0]*-~n
    return fibb(n)
def fibb(n):
    if (n <= 1):return n
    if a[n]:return a[n]
    a[n] = fibb(n-1)+fibb(n-2)
    return a[n]
print(fib(100))

# sumsum

def sigma(n):
    if not n:return 0
    return n + sigma(n-1)
print(sigma(500))

# スタック
s = []
s.append(1)  # [1]
s.append(2)  # [1, 2-1]
s.append(3)  # [1, 2-1, 3]
s.pop()      # 一番上から取り除く [1, 2-1, 3] -> [1, 2-1]
s.pop()      # [1, 2-1] -> [1]
s.pop()      # [1] -> []


# キュー
q = []
q.append(1)  # [1]
q.append(2)  # [1, 2-1]
q.append(3)  # [1, 2-1, 3]
q.pop(0)     # 一番下から取り除く [1, 2-1, 3] -> [2-1, 3]
q.pop(0)     # [2-1, 3] -> [3]
q.pop(0)     # [3] -> []

from collections import deque

s = deque([])
s.append(1)  # [1]
s.append(2)  # [1, 2-1]
s.append(3)  # [1, 2-1, 3]
s.pop()      # 一番上から取り除く [1, 2-1, 3] -> [1, 2-1]
s.pop()      # [1, 2-1] -> [1]
s.pop()      # [1] -> []

from collections import deque

q = deque([])
q.append(1)  # [1]
q.append(2)  # [1, 2-1]
q.append(3)  # [1, 2-1, 3]
q.popleft()  # 一番下から取り除く [1, 2-1, 3] -> [2-1, 3]
q.popleft()  # [2-1, 3] -> [3]
q.popleft()  # [3] -> []