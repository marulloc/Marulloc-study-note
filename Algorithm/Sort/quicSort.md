# 퀵정렬

### 파이썬 매운맛버전

```Python
n = int(input())
arr = list(map(int,input()))

def quick_sort(arr):
    if(len(arr)<=1): return arr

    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print("<",quick_sort(arr))
```
