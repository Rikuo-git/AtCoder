def bs(key):
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if s[mid] == key:
            return True
        elif key < s[mid]:
            right = mid
        else:
            left = mid + 1
    return False


n = int(input())
*s, = map(int, input().split())
input()
*t, = map(int, input().split())
print(sum(bs(i) for i in t))
