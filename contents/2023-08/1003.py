import sys

num_test = int(sys.stdin.readline())

fibo = [1, 0]

def add_fibo(x):
    while len(fibo) < x + 2:
        fibo.append(fibo[-1] + fibo[-2])

for _ in range(num_test):
    x = int(sys.stdin.readline())
    add_fibo(x)
    print(str(fibo[x]) + " " + str(fibo[x + 1]))
