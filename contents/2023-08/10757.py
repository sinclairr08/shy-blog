import sys

a, b = map(list, sys.stdin.readline().split())

idx_a = len(a) - 1
idx_b = len(b) - 1

sumList = []
over = 0

while idx_a >= 0 or idx_b >= 0:
    cur_a = int(a[idx_a]) if idx_a >= 0 else 0
    cur_b = int(b[idx_b]) if idx_b >= 0 else 0

    cur_sum = cur_a + cur_b + over

    if cur_sum > 9:
        cur_sum -= 10
        over = 1
    else:
        over = 0
    
    sumList.append(cur_sum)
    
    idx_a -= 1
    idx_b -= 1

if over == 1:
    sumList.append(over)

for i in range(len(sumList) - 1, -1, -1):
    print(sumList[i], end="")
